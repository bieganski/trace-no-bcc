#!/usr/bin/env python3

import ctypes
import platform
from enum import Enum, IntEnum, auto
import logging
from typing import Type

import gen.bpf as bpf

logging.basicConfig(level=logging.INFO)

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
    BPF_PROG_TEST_RUN = auto()
    BPF_PROG_RUN = auto()
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

def syscall_bpf_check_result_for_error(op: BPF_op, res: int):
    if op == bpf.BPF_PROG_LOAD:
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
    print(f"attr_addr={hex(attr_addr)}")
    res = syscall(ctypes.c_int(sys_bpf), ctypes.c_int(op), ctypes.c_ulong(attr_addr), ctypes.c_int(attr_size))
    syscall_bpf_check_result_for_error(op=op, res=res)
    return res

def alloc_writable_buf(type: Type[ctypes.Structure]) -> "ctypes._Pointer[ctypes.Structure]":
    size = ctypes.sizeof(type)
    assert size
    ptr = ctypes.create_string_buffer(init=bytes(size), size=size)
    return ctypes.cast(ptr, ctypes.POINTER(type))


def main():
    """
    bpf(BPF_PROG_LOAD, {
        prog_type=BPF_PROG_TYPE_KPROBE,
        insn_cnt=7,
        insns=0x64254dfa7950,
        license="Dual BSD/GPL",
        log_level=0,
        log_size=0,
        log_buf=NULL,
        kern_version=KERNEL_VERSION(6, 8, 12),
        prog_flags=0,
        prog_name="xdddwrite",
        prog_ifindex=0,
        expected_attach_type=BPF_CGROUP_INET_INGRESS,
        prog_btf_fd=4,
        func_info_rec_size=8,
        func_info=0x64254dfa6bc0,
        func_info_cnt=1,
        line_info_rec_size=16,
        line_info=0x64254dfa6be0,
        line_info_cnt=3,
        attach_btf_id=0,
        attach_prog_fd=0,
        fd_array=NULL}, 148) = 5
    """
    attr = bpf_prog_load__bpf_attr()

    minimal_insn_bytes = b"\xb7\x00\x00\x00\x00\x00\x00\x00\x95\x00\x00\x00\x00\x00\x00\x00"
    minimal_bpf_prog = ctypes.create_string_buffer(init=minimal_insn_bytes, size=len(minimal_insn_bytes))
    
    attr.prog_type = bpf.BPF_PROG_TYPE_KPROBE
    attr.insn_cnt = 2
    attr.insns = ctypes.cast(minimal_bpf_prog, ctypes.c_char_p) # ctypes.addressof(attr)  # XXX - whatever valid addr
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
    attr.prog_name = b"hehe"
    attr.prog_ifindex = 0
    attr.expected_attach_type=bpf.BPF_CGROUP_INET_INGRESS
    attr.prog_btf_fd = 4 # XXX
    attr.func_info_rec_size = 8 # XXX
    attr.func_info = 0 # ctypes.cast(buf, ctypes.c_char_p)
    attr.line_info_cnt = 0 # XXX

    attr.attach_btf_id = 0 # XXX
    attr.attach_prog_fd = 0 # XXX
    attr.fd_array = 0 # XXX

    # import time, os

    # while True:
    #     # license_ptr.contents = ctypes.c_ulong(0x66345678)
    #     a = license_ptr
    #     for addr in [ctypes.addressof(buf.contents)]:
    #         # print(f"sudo bash -c 'source common.alias ; rb /proc/{os.getpid()}/mem {hex(addr)} 20'")
    #         print(f"sudo gdb --batch -p {os.getpid()} -ex 'x/s {hex(addr)}' -ex quit")
    #     time.sleep(9999)

    res = syscall_bpf(
        op=BPF_op.BPF_PROG_LOAD,
        attr=attr,
    )

    print(f"bpf_prog_load fd={res}")
    import time
    print("sudo bpftool prog show")
    time.sleep(9999)

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    args = parser.parse_args()
    main()
