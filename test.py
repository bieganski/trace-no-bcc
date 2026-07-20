#!/usr/bin/env python3

import ctypes
import platform
from enum import Enum, IntEnum, auto
import logging
from typing import Type, Generator
from io import BytesIO
from pathlib import Path
import time

try:
    # XXX make IDE happy
    from .elfmanip import *
except:
    from elfmanip import find_section_or_raise, iter_relocations, find_relevant_relocation_sections, section_content
from blobmanip import op_write_bytes, WriteContext

from elftools.elf.elffile import ELFFile
from elftools.elf.sections import Symbol

from gen.libbpf import struct_perf_event_attr, struct_epoll_event
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
libc.mmap.restype = ctypes.c_void_p

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
    if res < 0:
        if hasattr(attr, "log_buf"):
            verifier_err_msg_bytes = ctypes.cast(attr.log_buf, ctypes.c_char_p).value
            raise RuntimeError("\n".join(str(verifier_err_msg_bytes).split(";")))
    syscall_bpf_check_result_for_error(op=op, res=res)
    return res

def alloc_writable_buf(type: Type[ctypes.Structure]) -> "ctypes._Pointer[ctypes.Structure]":
    size = ctypes.sizeof(type)
    assert size
    ptr = ctypes.create_string_buffer(init=bytes(size), size=size)
    return ctypes.cast(ptr, ctypes.POINTER(type))

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


# bpf(BPF_MAP_CREATE, {map_type=BPF_MAP_TYPE_RINGBUF, key_size=0, value_size=0, max_entries=262144, map_flags=0, inner_map_fd=0, map_name="rb", map_ifindex=0, btf_fd=10, btf_key_type_id=0, btf_value_type_id=0, btf_vmlinux_value_type_id=0, map_extra=0}, 72) = 11
# bpf(BPF_MAP_CREATE, {map_type=BPF_MAP_TYPE_RINGBUF, key_size=0, value_size=0, max_entries=1024  , map_flags=0, inner_map_fd=0, map_name="rb", map_ifindex=0, btf_fd=0, btf_key_type_id=0, btf_value_type_id=0, btf_vmlinux_value_type_id=0, map_extra=0}, 80) = -1 EINVAL (Invalid argument)

def bpf_ringbuf_create(max_entries: int, map_name: str) -> int:
    """
    returns fd
    """
    assert len(map_name) < 16
    assert (max_entries / 4096).is_integer()
    assert (max_entries / 4096) > 0
    attr = bpf_map_create__bpf_attr()
    attr.map_type = bpf.BPF_MAP_TYPE_RINGBUF
    attr.key_size = 0
    attr.value_size = 0
    attr.max_entries = max_entries
    attr.map_name = map_name.encode("ascii")
    fd = syscall_bpf(op=BPF_op.BPF_MAP_CREATE, attr=attr)
    logging.info(f"BPF map '{map_name}': BPF_MAP_CREATE OK")
    return fd

def _bpf_map_create_single_elem(size: int, map_name: str) -> int:
    """
    returns fd
    """
    assert len(map_name) < 16
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
    fd = _bpf_map_create_single_elem(size=len(init), map_name=map_name[:15])
    attr = bpf_map_update_elem__bpf_attr()
    attr.map_fd = fd
    attr.key = alloc_raw_buffer(data=b"\x00" * 8)
    attr.value = alloc_raw_buffer(data=init)
    logging.info(f"BPF_MAP_UPDATE_ELEM: raw pointer k={hex(attr.key)}, v={hex(attr.value)}")
    syscall_bpf(op=BPF_op.BPF_MAP_UPDATE_ELEM, attr=attr)
    logging.info(f"BPF map '{map_name}': BPF_MAP_UPDATE_ELEM OK")
    return fd

def relocate_section(elf_bytes: bytes, section_name: str) -> tuple[bytes, dict]:
    elf = ELFFile(BytesIO(elf_bytes))
    to_relocate = bytearray(elf.get_section_by_name(section_name).data())
    logging.info(f"relocating section '{section_name}' ({len(to_relocate)} bytes)..")
    logging.info(f"locating relocations corresponding to section '{section_name}'..")
    rel_sections = list(find_relevant_relocation_sections(elf_content=elf_bytes, section_name=section_name))
    # logging.info(f"sections with relocations corresponding to section '{section_name}: {[x.name for x in rel_sections]}")
    
    assert len(rel_sections) == 1
    bpf_maps : dict[str, int] = dict() # BPF map creation is lazy - only if some relocation refers section, the map for that section is created.
    for s in rel_sections:
        symtab_nr = s.sh_link
        symtab = elf.get_section(symtab_nr)
        logging.info(f"rel section '{section_name}': corresponding symbol table: '{symtab.name}' ({symtab_nr})")
        for i, reloc in enumerate(iter_relocations(elf_content=elf_bytes, sh=s)):
            if (reloc.r_info_type) != (R_BPF_64_64 := 1):
                raise NotImplementedError()
            symbol = symtab.get_symbol(symbol_idx := reloc.r_info_sym)
            if symbol.name:
                if symbol.name != "rb":
                    raise NotImplementedError()
                # if symbol['st_info']['type'] != 'STT_NOTYPE':
                #     raise NotImplementedError()
                map_name = symbol.name[-15:]
                if bpf_maps.get(map_name) is None:
                    fd = bpf_ringbuf_create(max_entries=256 * 1024, map_name=map_name)
                    bpf_maps[map_name] = fd
                else:
                    fd = bpf_maps[map_name]
            else:
                if symbol['st_info']['type'] != 'STT_SECTION':
                    raise NotImplementedError(symbol['st_info']['type'])
                __section_name = symbol_name_extract__quirk(elffile=elf, symbol=symbol)
                map_name = __section_name[-15:]

                if map_name not in bpf_maps:
                    logging.info(f"creating BPF map for section {__section_name}..")
                    section : bytes = elf.get_section_by_name(__section_name).data()
                    logging.info(f"section '{__section_name}' size={len(section)}")
                    fd = bpf_make_single_elem_map(init=section, map_name=map_name)
                    logging.info(f"section '{__section_name}': BPF map '{map_name}' created. For debug use 'sudo bpftool map dump name {map_name}'")
                    bpf_maps[map_name] = fd
                    time.sleep(99999)
                else:
                    logging.debug(f"skipping BPF map creation for section {__section_name} (reason: already there)")
                    fd = bpf_maps[map_name]

            logging.info(f"processing relocation {i}: offset={reloc.r_offset} (= 8 * {reloc.r_offset // 8}), symbol (st_name={symbol['st_name']})='{symbol.name or __section_name}' (sym_idx={symbol_idx})")
        
            # all modifications to 'insn' will be reflected in 'to_relocate' value.
            off = reloc.r_offset
            orig_insn = to_relocate[off:off + 8]
            insn = memoryview(to_relocate)[off:off + 8]
            insn = bpf.struct_bpf_insn.from_buffer(insn)
            imm64 = memoryview(to_relocate)[off + 8:off + 16]  # next instruction slot
            imm64_insn = bpf.struct_bpf_insn.from_buffer(imm64)
            assert insn.code == 0x18
            assert insn.src_reg == 0
            assert insn.off == 0
            # actually rewrite.
            imm64_insn.imm = insn.imm
            insn.imm = fd
            if map_name != "rb":
                insn.src_reg = bpf.BPF_PSEUDO_MAP_VALUE
            else:
                insn.src_reg = bpf.BPF_PSEUDO_MAP_FD

            logging.info(f"rewritten insn {orig_insn.hex()} into {bytes(insn).hex()}. following imm64={bytes(imm64).hex()}")
    return bytes(to_relocate), bpf_maps

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
    attr.log_level = 11
    attr.log_size = 10000
    attr.log_buf = ctypes.cast(ctypes.create_string_buffer(10000), ctypes.c_void_p).value
    # raise ValueError(hex(attr.log_buf))
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
    logging.info(f"uprobe_perf_event_open: {elf}:{hex(offset)}, retprobe={is_retprobe}")
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

def create_epoll_event(rb_fd: int) -> int:
    epoll_fd = libc.epoll_create1(EPOLL_CLOEXEC := 0x80000)
    if epoll_fd < 0:
        raise RuntimeError(f"epoll_create1: {errno()}")
    # strace libbpf:
    # epoll_ctl(16<anon_inode:[eventpoll]>, EPOLL_CTL_ADD, 3<anon_inode:bpf-map>, {events=EPOLLIN, data={u32=0, u64=0}}) = 0
    # epoll_ctl(0x10, 0x1, 0x3, 0x626ee9b720e0) = 0
    epoll_event = struct_epoll_event()
    epoll_event.events = (EPOLLIN := 0x1)
    if libc.epoll_ctl(epoll_fd, EPOLL_CTL_ADD := 0x1, rb_fd, ctypes.byref(epoll_event)) != 0:
        raise RuntimeError(f"epoll_ctl: {errno()}")
    return epoll_fd

# kernel/bpf/ringbuf.c
class BpfRingbufHdr(ctypes.Structure):
    _fields_ = [
        ("len", ctypes.c_uint32),
        ("pg_off", ctypes.c_uint32),
    ]

class struct_pt_regs_riscv64(ctypes.Structure):
    _fields_ = [
        ('epc', ctypes.c_ulong),
        ('ra', ctypes.c_ulong),
        ('sp', ctypes.c_ulong),
        ('gp', ctypes.c_ulong),
        ('tp', ctypes.c_ulong),
        ('t0', ctypes.c_ulong),
        ('t1', ctypes.c_ulong),
        ('t2', ctypes.c_ulong),
        ('s0', ctypes.c_ulong),
        ('s1', ctypes.c_ulong),
        ('a0', ctypes.c_ulong),
        ('a1', ctypes.c_ulong),
        ('a2', ctypes.c_ulong),
        ('a3', ctypes.c_ulong),
        ('a4', ctypes.c_ulong),
        ('a5', ctypes.c_ulong),
        ('a6', ctypes.c_ulong),
        ('a7', ctypes.c_ulong),
        ('s2', ctypes.c_ulong),
        ('s3', ctypes.c_ulong),
        ('s4', ctypes.c_ulong),
        ('s5', ctypes.c_ulong),
        ('s6', ctypes.c_ulong),
        ('s7', ctypes.c_ulong),
        ('s8', ctypes.c_ulong),
        ('s9', ctypes.c_ulong),
        ('s10', ctypes.c_ulong),
        ('s11', ctypes.c_ulong),
        ('t3', ctypes.c_ulong),
        ('t4', ctypes.c_ulong),
        ('t5', ctypes.c_ulong),
        ('t6', ctypes.c_ulong),
        ('status', ctypes.c_ulong),
        ('badaddr', ctypes.c_ulong),
        ('cause', ctypes.c_ulong),
        ('orig_a0', ctypes.c_ulong),
    ]

class struct_pt_regs_x86_64(ctypes.Structure):
    _fields_ = [
        ('r15', ctypes.c_ulong),
        ('r14', ctypes.c_ulong),
        ('r13', ctypes.c_ulong),
        ('r12', ctypes.c_ulong),
        ('bp', ctypes.c_ulong),
        ('bx', ctypes.c_ulong),
        ('r11', ctypes.c_ulong),
        ('r10', ctypes.c_ulong),
        ('r9', ctypes.c_ulong),
        ('r8', ctypes.c_ulong),
        ('ax', ctypes.c_ulong),
        ('cx', ctypes.c_ulong),
        ('dx', ctypes.c_ulong),
        ('si', ctypes.c_ulong),
        ('di', ctypes.c_ulong),
        ('orig_ax', ctypes.c_ulong),
        ('ip', ctypes.c_ulong),
        ('cs', ctypes.c_ulong),
        ('flags', ctypes.c_ulong),
        ('sp', ctypes.c_ulong),
        ('ss', ctypes.c_ulong),
    ]

class struct_pt_regs_armv7l(ctypes.Union):
    _fields_ = [
        ("uregs", ctypes.c_uint32 * 18),
    ]

class union_pt_regs(ctypes.Union):
    _fields_ = [
        ("x86_64", struct_pt_regs_x86_64),
        ("riscv64", struct_pt_regs_riscv64),
        ("armv7l", struct_pt_regs_armv7l),
    ]

# Define the struct event in Python
class Event(ctypes.Structure):
    _fields_ = [
        ("library_path", ctypes.c_char * 128),
        ("symbol_name", ctypes.c_char * 64),
        ("pid", ctypes.c_int32),
        ("tid", ctypes.c_int32),

        ("timestamp",   ctypes.c_uint64),
        ("is_ret",      ctypes.c_int32),

        ("pt_regs_union", union_pt_regs)
    ]


def get_regs_of_interest(arch: CPU_Arch, is_ret: bool) -> list[str]:
    if arch == CPU_Arch.x86_64:
        return ["ax"] if is_ret else ["di", "si", "dx", "cx", "r8", "r9", "r10"]
    elif arch == CPU_Arch.riscv64:
        return ["a0"] if is_ret else ["ra"] + [f"a{i}" for i in range(7)]
    elif arch == CPU_Arch.armv7l:
        return [] # TODO
    else:
        assert False

def fmt_regs(reg_names: list[str], pt_regs: ctypes.Structure) -> str:
    res = ""
    for i, name in enumerate(reg_names):
        res += f"{name}={hex(getattr(pt_regs, name))}"
        if not (last := i == len(reg_names) - 1):
            res += ", "
    return res


def print_event(event: Event):
    lib_basename = event.library_path.decode("ascii", errors="ignore").split("/")[-1]
    symbol_name = event.symbol_name.decode("ascii", errors="ignore")

    arch = system_get_cpu_arch()

    pt_regs = getattr(event.pt_regs_union, system_get_cpu_arch().value)

    msg_prefix =  f"[{event.timestamp}]"
    msg_prefix += f"[{event.pid},{event.tid}][{lib_basename}:{symbol_name}]"

    regs_str = fmt_regs(reg_names=get_regs_of_interest(arch=arch, is_ret=event.is_ret), pt_regs=pt_regs)

    print(f"{msg_prefix} {regs_str}")

def main():
    from pathlib import Path
    bpf_elf_bytes = (Path(__file__).parent / "uprobe.bpf.o").read_bytes()
    bpf_elf_bytes = bpf_elf_adjust_to_cpu_arch(elf_bytes=bpf_elf_bytes)
    ebpf_programs = elf_iter_symbols(elf_bytes=bpf_elf_bytes)

    logging.info(f"eBPF programs found: {ebpf_programs}") # XXX - offsets from what??
    code, bpf_maps = relocate_section(elf_bytes=bpf_elf_bytes, section_name="uprobe//")
    assert (rb_map_fd := bpf_maps.get("rb")) is not None
    del bpf_maps
    
    traced_elf_path = Path("/lib/x86_64-linux-gnu/libc.so.6")
    traced_symbol = "clock_nanosleep"
    traced_symbol_offset = symbol_offset_and_size(elf_bytes=traced_elf_path.read_bytes(), symbol=traced_symbol)[0]
    for prog_name, (offset, size) in ebpf_programs.items():
        prog_code = code[offset:offset + size]
        prog_fd = bpf_prog_load(code=prog_code, prog_name=prog_name)
        event_fd = uprobe_perf_event_open(
            elf=traced_elf_path,
            offset=traced_symbol_offset,
            is_retprobe=program_is_retprobe(symbol=prog_name),
        )
        bpf_link_create(prog_fd=prog_fd, perf_event_fd=event_fd)

    print("$    sudo bpftool prog show")
    print("$    sudo cat /sys/kernel/debug/tracing/trace_pipe")
    
    epoll_fd = create_epoll_event(rb_fd=rb_map_fd)
    epoll_state = struct_epoll_event()
    num_events, timeout_ms = 1, -1

    mmap_1st_page_ptr = libc.mmap((_addr := 0x0), (_length := 4096), (PROT_READ := 0x1) | (PROT_WRITE := 0x2), (MAP_SHARED := 0x1), rb_map_fd, (_offset := 0))
    assert mmap_1st_page_ptr > 0, mmap_1st_page_ptr
    assert ctypes.c_uint64.from_address(mmap_1st_page_ptr).value == 0x0

    mmap_2nd_page_ptr = libc.mmap((_addr := 0x0), (_length := 4096 * 2), (PROT_READ := 0x1), (MAP_SHARED := 0x1), rb_map_fd, (_offset := 4096))
    # raise ValueError((ctypes.c_char * 256).from_address(mmap_2nd_page_ptr + 4096).raw)

    while True:
        match libc.epoll_wait(epoll_fd, ctypes.byref(epoll_state), num_events, timeout_ms):
            case 1:
                assert epoll_state.events == (EPOLLIN := 0x1)
                consumer_pos = ctypes.c_uint64.from_address(mmap_1st_page_ptr).value
                print("consumer_pos=", consumer_pos)
                time.sleep(2)
                hdr_addr = mmap_2nd_page_ptr + 4096 + consumer_pos
                hdr = BpfRingbufHdr.from_address(hdr_addr)
                assert hdr.len == ctypes.sizeof(Event)
                new_consumer_pos = consumer_pos + ctypes.sizeof(BpfRingbufHdr) + hdr.len
                ev = Event.from_address(hdr_addr + ctypes.sizeof(BpfRingbufHdr))
                print_event(ev)
                ctypes.c_uint64.from_address(mmap_1st_page_ptr).value = new_consumer_pos
            case 0:
                assert False
            case -1:
                raise RuntimeError(f"epoll_wait: {errno()}")

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    args = parser.parse_args()
    main()
