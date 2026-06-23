#!/usr/bin/env python3

import ctypes
import platform
from enum import Enum, IntEnum, auto
import logging
from typing import Type, Generator
from io import BytesIO
from pathlib import Path

from elfmanip import find_section_or_raise
from blobmanip import op_write_bytes, WriteContext

from elftools.elf.elffile import ELFFile
from elftools.elf.sections import Symbol

from gen.libbpf import struct_perf_event_attr
import gen.bpf as bpf

from inspect import getmembers
from pprint import pformat
x = lambda y: pformat(getmembers(y))

assert 8 == ctypes.sizeof(bpf.struct_bpf_insn)
insn = bpf.struct_bpf_insn()
insn.imm = 3
assert bytes(insn) == b'\x00\x00\x00\x00\x03\x00\x00\x00'
one = b'\x00\x00\x00\x00\x00\x00\x00\xf0'
assert ctypes.c_uint64.from_buffer_copy(one).value == 0xf000_0000_0000_0000

logging.basicConfig(level=logging.DEBUG)

libc = ctypes.CDLL(None)
syscall = libc.syscall

class CPU_Arch(Enum):
    x86_64 = "x86_64"
    riscv64 = "riscv64"
    armv7l = "armv7l"

def system_get_cpu_arch() -> CPU_Arch:
    machine = platform.machine()
    return CPU_Arch(machine)

get_errno_loc = libc.__errno_location
get_errno_loc.restype = ctypes.POINTER(ctypes.c_int)

def errno():
    e: int = get_errno_loc()[0]
    import errno
    return errno.errorcode[e]

bpf_syscall_nr = {
    CPU_Arch.x86_64: 321,
    CPU_Arch.riscv64: 280,
    CPU_Arch.armv7l: 386,
}

perf_event_open_syscall_nr = {
    CPU_Arch.x86_64: 298,
    CPU_Arch.riscv64: 241,
    CPU_Arch.armv7l: 241,
}

class BPF_op(IntEnum):
    """
    copy-pasted from gen/bpf.py
    """
    BPF_MAP_CREATE = 0
    BPF_MAP_LOOKUP_ELEM = auto()
    BPF_MAP_UPDATE_ELEM = auto()
    BPF_MAP_DELETE_ELEM = auto()
    BPF_MAP_GET_NEXT_KEY = auto()
    BPF_PROG_LOAD = auto()
    BPF_OBJ_PIN = auto()
    BPF_OBJ_GET = auto()
    BPF_PROG_ATTACH = auto()
    BPF_PROG_DETACH = auto()
    BPF_PROG_TEST_RUN = 10
    BPF_PROG_RUN = 10
    BPF_PROG_GET_NEXT_ID = auto()
    BPF_MAP_GET_NEXT_ID = auto()
    BPF_PROG_GET_FD_BY_ID = auto()
    BPF_MAP_GET_FD_BY_ID = auto()
    BPF_OBJ_GET_INFO_BY_FD = auto()
    BPF_PROG_QUERY = auto()
    BPF_RAW_TRACEPOINT_OPEN = auto()
    BPF_BTF_LOAD = auto()
    BPF_BTF_GET_FD_BY_ID = auto()
    BPF_TASK_FD_QUERY = auto()
    BPF_MAP_LOOKUP_AND_DELETE_ELEM = auto()
    BPF_MAP_FREEZE = auto()
    BPF_BTF_GET_NEXT_ID = auto()
    BPF_MAP_LOOKUP_BATCH = auto()
    BPF_MAP_LOOKUP_AND_DELETE_BATCH = auto()
    BPF_MAP_UPDATE_BATCH = auto()
    BPF_MAP_DELETE_BATCH = auto()
    BPF_LINK_CREATE = auto()
    BPF_LINK_UPDATE = auto()
    BPF_LINK_GET_FD_BY_ID = auto()
    BPF_LINK_GET_NEXT_ID = auto()
    BPF_ENABLE_STATS = auto()
    BPF_ITER_CREATE = auto()
    BPF_LINK_DETACH = auto()
    BPF_PROG_BIND_MAP = auto()
    BPF_TOKEN_CREATE = auto()

bpf_prog_load__bpf_attr = bpf.struct_anon_17
bpf_map_create__bpf_attr = bpf.struct_anon_12
bpf_map_update_elem__bpf_attr = bpf.struct_anon_14
bpf_link_create__bpf_attr = bpf.struct_anon_45

def syscall_bpf_check_result_for_error(op: BPF_op, res: int):
    if op in [bpf.BPF_PROG_LOAD, bpf.BPF_MAP_CREATE, bpf.BPF_MAP_UPDATE_ELEM, bpf.BPF_LINK_CREATE]:
        if res == -1:
            raise RuntimeError(f"{op.name}: {errno()}")
        else:
            logging.info(f"{op.name} OK")
    else:
        assert False

def syscall_bpf(op: BPF_op, attr: ctypes.Union):
    assert isinstance(op, BPF_op)
    sys_bpf : int = bpf_syscall_nr[system_get_cpu_arch()]
    attr_addr, attr_size = ctypes.addressof(attr), ctypes.sizeof(attr)
    logging.info(f"bpf(op={op.name}, attr={hex(attr_addr)}, size={attr_size})")
    logging.debug(f"attr_addr={hex(attr_addr)}")
    res = syscall(ctypes.c_int(sys_bpf), ctypes.c_int(op), ctypes.c_ulong(attr_addr), ctypes.c_int(attr_size))
    syscall_bpf_check_result_for_error(op=op, res=res)
    return res

def alloc_writable_buf(type: Type[ctypes.Structure]) -> "ctypes._Pointer[ctypes.Structure]":
    size = ctypes.sizeof(type)
    assert size
    ptr = ctypes.create_string_buffer(init=bytes(size), size=size)
    return ctypes.cast(ptr, ctypes.POINTER(type))

def find_all_relocation_sections(elf: ELFFile) -> Generator:
    for section in elf.iter_sections():
        # Check if this is a relocation section
        if section.header.sh_type not in ('SHT_REL', 'SHT_RELA'):
            continue
        yield section

def find_relevant_relocation_sections(elf: ELFFile, section_name: str) -> Generator:
    for s in find_all_relocation_sections(elf=elf):
        target_section_idx = s.header.sh_info
        if elf.get_section(target_section_idx).name == section_name:
            yield s

def symbol_name_extract__quirk(elffile: ELFFile, symbol: Symbol) -> str:
    """
    Took from pyelftools/scripts/readelf.py.
    """
    symbol_name = symbol.name
    if (symbol['st_info']['type'] == 'STT_SECTION'
        and symbol['st_shndx'] != 'SHN_UNDEF'
        and symbol['st_shndx'] < elffile.num_sections()
        and symbol['st_name'] == 0):
        symbol_name = elffile.get_section(symbol['st_shndx']).name
    assert symbol_name
    return symbol_name

def alloc_raw_buffer(data: bytes) -> int:
    """
    returns raw buffer address, see '__debug_gdb' for details.
    """
    assert isinstance(data, bytes)
    val_ptr = ctypes.create_string_buffer(init=data, size=len(data))
    val_ptr = ctypes.cast(val_ptr, ctypes.POINTER(ctypes.c_char))
    return ctypes.addressof(val_ptr.contents)

def __debug_gdb(data: bytes = b"\xde\xad\xbe\xef\00\x11\x22\x33"):
    import time
    import os
    addr = alloc_raw_buffer(data=data)
    print("*", hex(addr), "=", data)
    print(f"sudo gdb --batch -p {os.getpid()} -ex 'x/{1 + len(data) // 8}x {hex(addr)}' -ex quit")
    time.sleep(9999)


def _bpf_map_create_single_elem(size: int, map_name: str) -> int:
    """
    returns fd
    """
    attr = bpf_map_create__bpf_attr()
    attr.map_type = bpf.BPF_MAP_TYPE_ARRAY
    attr.key_size = 4
    attr.value_size = size
    attr.max_entries = 1
    attr.map_flags = 0 # XXX possibly READ_ONLY
    attr.map_name = map_name.encode("ascii")
    fd = syscall_bpf(op=BPF_op.BPF_MAP_CREATE, attr=attr)
    logging.info(f"BPF map '{map_name}': BPF_MAP_CREATE OK")
    return fd


def bpf_make_single_elem_map(init: bytes, map_name: str) -> int:
    """
    returns fd of newly created BPF map.
    """
    fd = _bpf_map_create_single_elem(size=len(init), map_name=map_name)
    attr = bpf_map_update_elem__bpf_attr()
    attr.map_fd = fd
    attr.key = alloc_raw_buffer(data=b"\x00" * 8)
    attr.value = alloc_raw_buffer(data=init)
    logging.info(f"BPF_MAP_UPDATE_ELEM: raw pointer k={hex(attr.key)}, v={hex(attr.value)}")
    syscall_bpf(op=BPF_op.BPF_MAP_UPDATE_ELEM, attr=attr)
    logging.info(f"BPF map '{map_name}': BPF_MAP_UPDATE_ELEM OK")
    return fd

def relocate_section(elf_bytes: bytes, section_name: str) -> bytes:
    elf = ELFFile(BytesIO(elf_bytes))
    to_relocate = bytearray(elf.get_section_by_name(section_name).data())
    logging.info(f"relocating section '{section_name}' ({len(to_relocate)} bytes)..")
    logging.info(f"locating relocations corresponding to section '{section_name}'..")
    rel_sections = list(find_relevant_relocation_sections(elf=elf, section_name=section_name))
    logging.info(f"sections with relocations corresponding to section '{section_name}: {[x.name for x in rel_sections]}")
    
    assert len(rel_sections) == 1
    bpf_maps : dict[str, int] = dict() # BPF map creation is lazy - only if some relocation refers section, the map for that section is created.
    for s in rel_sections:
        symtab_nr = s['sh_link']
        symtab = elf.get_section(symtab_nr)
        logging.info(f"rel section '{s.name}': corresponding symbol table: '{symtab.name}' ({symtab_nr})")
        for i, reloc in enumerate(s.iter_relocations()):
            if (reloc['r_info_type']) != (R_BPF_64_64 := 1):
                raise NotImplementedError()
            symbol = symtab.get_symbol(symbol_idx := reloc['r_info_sym'])
            if symbol.name:
                raise NotImplementedError()
            if symbol['st_info']['type'] != 'STT_SECTION':
                raise NotImplementedError()
            symbol_name = symbol_name_extract__quirk(elffile=elf, symbol=symbol)

            logging.info(f"processing relocation {i}: offset={reloc['r_offset']}, symbol (st_name={symbol['st_name']})='{symbol_name}' (sym_idx={symbol_idx})")

            if (map_name := f"_map_{symbol_name}") not in bpf_maps:
                logging.info(f"creating BPF map for section {symbol_name}..")
                section : bytes = elf.get_section_by_name(symbol_name).data()
                logging.info(f"section '{symbol_name}' size={len(section)}")
                fd = bpf_make_single_elem_map(init=section, map_name=map_name)
                logging.info(f"section '{symbol_name}': BPF map '{map_name}' created. For debug use 'sudo bpftool map dump name {map_name}'")
                bpf_maps[map_name] = fd
            else:
                logging.debug(f"skipping BPF map creation for section {symbol_name} (reason: already there)")
                fd = bpf_maps[map_name]
        
            # all modifications to 'insn' will be reflected in 'to_relocate' value.
            off = reloc['r_offset']
            orig_insn = to_relocate[off:off + 8]
            insn = memoryview(to_relocate)[off:off + 8]
            insn = bpf.struct_bpf_insn.from_buffer(insn)
            assert insn.code == 0x18
            assert insn.src_reg == 0
            assert insn.off == 0
            imm64 = memoryview(to_relocate)[off + 8:off + 16]  # next "instruction"
            assert insn.imm <= 255
            imm64[0] = insn.imm
            insn.imm = fd
            insn.src_reg = bpf.BPF_PSEUDO_MAP_VALUE

            logging.info(f"rewritten insn {orig_insn} into {[hex(x) for x in bytes(insn)]}, and following imm64={bytes(imm64)}")
    return bytes(to_relocate)

def float2int_safe(val: float) -> int:
    assert val.is_integer()
    return int(val)

def bpf_prog_load(code: bytes, prog_name: str):
    """
    'code' needs to be relocated (and corresponding map file descriptors opened).
    returns file descriptor of loaded program.
    """

    attr = bpf_prog_load__bpf_attr()
    ctypes_code = ctypes.create_string_buffer(init=code, size=len(code))

    attr.prog_type = bpf.BPF_PROG_TYPE_KPROBE
    attr.insn_cnt = float2int_safe(len(ctypes_code) / 8)
    attr.insns = ctypes.cast(ctypes_code, ctypes.c_void_p).value
    # license_ptr = ctypes.create_string_buffer(init=b"Dual BSD/GPL", size=len(b"Dual BSD/GPL")),
    # buf = alloc_writable_buf(type=ctypes.c_char * 12, )
    # buf = ctypes.cast(buf, ctypes.c_void_p)
    # buf.contents = b"Dual BSD/GPL"
    buf = ctypes.create_string_buffer(init=b"Dual BSD/GPL", size=len(b"Dual BSD/GPL"))
    buf = ctypes.cast(buf, ctypes.POINTER(ctypes.c_char * 1000000000000))
    # license_ptr = ctypes.cast(buf, ctypes.POINTER(ctypes.c_ulong))
    # license_ptr_as_ulong = ctypes.cast(buf, ctypes.POINTER(ctypes.c_ulong))
    attr.license = ctypes.cast(buf, ctypes.c_char_p) # ctypes.cast(license_ptr, ctypes.c_void_p) # license_ptr_as_ulong
    attr.log_level = 0
    attr.log_size = 0
    attr.log_buf = 0 # or ctypes.POINTER(ctypes.c_char)()?
    KERNEL_VERSION = lambda a, b, c: (((a) << 16) + ((b) << 8) + (c))
    attr.kern_version = KERNEL_VERSION(6, 17, 0)
    attr.prog_flags = 0
    attr.prog_name = prog_name[:15].encode("ascii")
    attr.prog_ifindex = 0
    attr.expected_attach_type=bpf.BPF_CGROUP_INET_INGRESS
    attr.prog_btf_fd = 4 # XXX
    attr.func_info_rec_size = 8 # XXX
    attr.func_info = 0 # ctypes.cast(buf, ctypes.c_char_p)
    attr.line_info_cnt = 0 # XXX

    attr.attach_btf_id = 0 # XXX
    attr.attach_prog_fd = 0 # XXX
    attr.fd_array = 0 # XXX

    res = syscall_bpf(
        op=BPF_op.BPF_PROG_LOAD,
        attr=attr,
    )
    return res

def syscall_perf_event_open(attr: ctypes.Structure, pid: int = -1, cpu: int = 0) -> int:
    """
    'pid' and 'cpu' semantics explained at https://man7.org/linux/man-pages/man2/perf_event_open.2.html
    int syscall(SYS_perf_event_open, struct perf_event_attr *attr, pid_t pid, int cpu, int group_fd, unsigned long flags);
    """
    sys_perf_event_open : int = perf_event_open_syscall_nr[system_get_cpu_arch()]
    group_fd = ctypes.c_int(group_leader := -1)
    flags = ctypes.c_int(PERF_FLAG_FD_CLOEXEC := 8)
    res = syscall(
        ctypes.c_int(sys_perf_event_open),
        ctypes.c_ulong(ctypes.addressof(attr)),
        ctypes.c_int(pid),
        ctypes.c_int(cpu),
        group_fd,
        flags,
    )
    logging.info(f"perf_event_open()")
    return res

def bpf_link_create(prog_fd: int, perf_event_fd: int) -> int:
    """
    returns fd
    """
    attr = bpf_link_create__bpf_attr()
    attr.attach_type = ctypes.c_uint32(bpf.BPF_PERF_EVENT)
    attr.unnamed_anon_45_1 = bpf.union_anon_32()
    attr.unnamed_anon_45_1.prog_fd = ctypes.c_uint32(prog_fd)
    attr.unnamed_anon_45_2 = bpf.union_anon_33()
    attr.unnamed_anon_45_2.target_fd = ctypes.c_uint32(perf_event_fd)
    fd = syscall_bpf(op=BPF_op.BPF_LINK_CREATE, attr=attr)
    logging.info(f"bpf(BPF_LINK_CREATE) ok")
    return fd


def uprobe_perf_event_open(elf: Path, offset: int, is_retprobe: bool) -> int:
    logging.info(f"uprobe_perf_event_open: {elf}:{offset}, retprobe={is_retprobe}")
    attr = struct_perf_event_attr()
    attr.type = (UPROBE_EVENT_TYPE := 0x9)
    attr.size = ctypes.sizeof(struct_perf_event_attr)
    path : bytes = str(elf.expanduser().resolve().absolute()).encode("ascii")
    ctypes_path = alloc_raw_buffer(path)

    assert attr.size == 0x88
    attr.uprobe_path = ctypes_path
    attr.kprobe_func = ctypes_path
    attr.kprobe_addr = offset
    attr.probe_offset = offset
    attr.config2 = offset
    attr.config = (1 if is_retprobe else 0) << determine_retprobe_bit(uprobe_not_kprobe=True)
    fd = syscall_perf_event_open(attr)
    if fd < 0:
        raise RuntimeError(f"perf_event_open: FAILED: {errno()}")
    return fd

def bpf_elf_adjust_to_cpu_arch(elf_bytes: bytes, native_arch : CPU_Arch = system_get_cpu_arch()) -> bytes:

    for arch in CPU_Arch:
        sec_name = f".rodata.arch_is_{arch.value}"
        arch_section = find_section_or_raise(elf_content=elf_bytes, sec_name=sec_name)
        assert arch_section.content_length == 4

        val = bytes(ctypes.c_uint32(1 if arch == native_arch else 0))

        logging.info(f"writing {val} to section '{sec_name}' (off={hex(arch_section.sh_offset)})")

        op = WriteContext(offset=arch_section.content_file_offset, bytes_to_write=val)
        elf_bytes = op_write_bytes(context=op, input_data=elf_bytes)

    return elf_bytes


def determine_retprobe_bit(uprobe_not_kprobe: bool) -> int:
    """
    libbpf reads from /sys/bus/event_source/devices/{uprobe|kprobe}/format/retprobe,
    we go yolo with hardcoded value.
    """
    return 0

def program_is_retprobe(symbol: str) -> bool:
    return "ret" in symbol

def elf_iter_symbols(elf_bytes: bytes) -> dict[str, tuple[int, int]]:
    """
    returns a map from symbol (program) name to (file offset, size in bytes).
    size in bytes will be positive integer, divisible by 8 (eBPF instruction size).
    """
    elf_file = ELFFile(BytesIO(elf_bytes))
    from elftools.elf.sections import SymbolTableSection
    symbol_tables = [s for s in elf_file.iter_sections() if isinstance(s, SymbolTableSection)]
    assert len(symbol_tables) == 1
    res = dict()
    for section in symbol_tables:
        for symbol in section.iter_symbols():
            if symbol['st_info']['type'] == "STT_FUNC":
                res[symbol.name] = (symbol["st_value"], symbol['st_size'])
    return res

def symbol_offset_and_size(symbol: str, elf_bytes: bytes) -> tuple[int, int]:
    map = elf_iter_symbols(elf_bytes=elf_bytes)
    if symbol not in map:
        raise RuntimeError(f"could not find symbol {symbol}!")
    offset, size = map[symbol]
    logging.info(f"located symbol '{symbol}' at offset={hex(offset)} and size={hex(size)}")
    return offset, size

def main():
    from pathlib import Path
    bpf_elf_bytes = Path("uprobe.bpf.o").read_bytes()
    bpf_elf_bytes = bpf_elf_adjust_to_cpu_arch(elf_bytes=bpf_elf_bytes)
    ebpf_programs = elf_iter_symbols(elf_bytes=bpf_elf_bytes)
    logging.info(f"eBPF programs found: {ebpf_programs}") # XXX - offsets from what??
    code : bytes = relocate_section(elf_bytes=bpf_elf_bytes, section_name="uprobe//")
    
    traced_elf_path = Path("/lib/x86_64-linux-gnu/libc.so.6")
    traced_symbol = "malloc"
    traced_symbol_offset = symbol_offset_and_size(elf_bytes=traced_elf_path.read_bytes(), symbol=traced_symbol)[0]
    for prog_name, (offset, size) in ebpf_programs.items():
        prog_code = code[offset:offset + size]
        if not program_is_retprobe(symbol=prog_name):
            continue # XXX
        prog_fd = bpf_prog_load(code=prog_code, prog_name=prog_name)
        event_fd = uprobe_perf_event_open(
            elf=traced_elf_path,
            offset=traced_symbol_offset,
            is_retprobe=False, # program_is_retprobe(symbol=prog_name),
        )
        bpf_link_create(prog_fd=prog_fd, perf_event_fd=event_fd)

    print("$    sudo bpftool prog show")
    print("$    sudo cat /sys/kernel/debug/tracing/trace_pipe")
    import time
    time.sleep(9999)


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    args = parser.parse_args()
    main()
