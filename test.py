#!/usr/bin/env python3

import ctypes
import platform
from enum import Enum, IntEnum

import gen.bpf as bpf

libc = ctypes.CDLL(None)
syscall = libc.syscall

class CPU_Arch(Enum):
    x86_64 = "x86_64"
    riscv64 = "riscv64"
    armv7l = "armv7l"

def system_get_cpu_arch() -> CPU_Arch:
    machine = platform.machine()
    return CPU_Arch(machine)


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
    BPF_MAP_LOOKUP_ELEM = (BPF_MAP_CREATE + 1)
    BPF_MAP_UPDATE_ELEM = (BPF_MAP_LOOKUP_ELEM + 1)
    BPF_MAP_DELETE_ELEM = (BPF_MAP_UPDATE_ELEM + 1)
    BPF_MAP_GET_NEXT_KEY = (BPF_MAP_DELETE_ELEM + 1)
    BPF_PROG_LOAD = (BPF_MAP_GET_NEXT_KEY + 1)
    BPF_OBJ_PIN = (BPF_PROG_LOAD + 1)
    BPF_OBJ_GET = (BPF_OBJ_PIN + 1)
    BPF_PROG_ATTACH = (BPF_OBJ_GET + 1)
    BPF_PROG_DETACH = (BPF_PROG_ATTACH + 1)
    BPF_PROG_TEST_RUN = (BPF_PROG_DETACH + 1)
    BPF_PROG_RUN = BPF_PROG_TEST_RUN
    BPF_PROG_GET_NEXT_ID = (BPF_PROG_RUN + 1)
    BPF_MAP_GET_NEXT_ID = (BPF_PROG_GET_NEXT_ID + 1)
    BPF_PROG_GET_FD_BY_ID = (BPF_MAP_GET_NEXT_ID + 1)
    BPF_MAP_GET_FD_BY_ID = (BPF_PROG_GET_FD_BY_ID + 1)
    BPF_OBJ_GET_INFO_BY_FD = (BPF_MAP_GET_FD_BY_ID + 1)
    BPF_PROG_QUERY = (BPF_OBJ_GET_INFO_BY_FD + 1)
    BPF_RAW_TRACEPOINT_OPEN = (BPF_PROG_QUERY + 1)
    BPF_BTF_LOAD = (BPF_RAW_TRACEPOINT_OPEN + 1)
    BPF_BTF_GET_FD_BY_ID = (BPF_BTF_LOAD + 1)
    BPF_TASK_FD_QUERY = (BPF_BTF_GET_FD_BY_ID + 1)
    BPF_MAP_LOOKUP_AND_DELETE_ELEM = (BPF_TASK_FD_QUERY + 1)
    BPF_MAP_FREEZE = (BPF_MAP_LOOKUP_AND_DELETE_ELEM + 1)
    BPF_BTF_GET_NEXT_ID = (BPF_MAP_FREEZE + 1)
    BPF_MAP_LOOKUP_BATCH = (BPF_BTF_GET_NEXT_ID + 1)
    BPF_MAP_LOOKUP_AND_DELETE_BATCH = (BPF_MAP_LOOKUP_BATCH + 1)
    BPF_MAP_UPDATE_BATCH = (BPF_MAP_LOOKUP_AND_DELETE_BATCH + 1)
    BPF_MAP_DELETE_BATCH = (BPF_MAP_UPDATE_BATCH + 1)
    BPF_LINK_CREATE = (BPF_MAP_DELETE_BATCH + 1)
    BPF_LINK_UPDATE = (BPF_LINK_CREATE + 1)
    BPF_LINK_GET_FD_BY_ID = (BPF_LINK_UPDATE + 1)
    BPF_LINK_GET_NEXT_ID = (BPF_LINK_GET_FD_BY_ID + 1)
    BPF_ENABLE_STATS = (BPF_LINK_GET_NEXT_ID + 1)
    BPF_ITER_CREATE = (BPF_ENABLE_STATS + 1)
    BPF_LINK_DETACH = (BPF_ITER_CREATE + 1)
    BPF_PROG_BIND_MAP = (BPF_LINK_DETACH + 1)
    BPF_TOKEN_CREATE = (BPF_PROG_BIND_MAP + 1)

def syscall_bpf_res_handler(op: BPF_op, res: int):
    if op == bpf.BPF_PROG_LOAD:
        if res == -1:
            raise RuntimeError(f"{op.name}: EPERM")

def syscall_bpf(op: BPF_op, *args):
    assert isinstance(op, BPF_op)
    sys_bpf : int = bpf_syscall_nr[system_get_cpu_arch()]
    res = syscall(sys_bpf, op, *args)
    syscall_bpf_res_handler(op=op, res=res)
    return res

def main():
    res = syscall_bpf(
        op=BPF_op.BPF_PROG_LOAD,
    )

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    args = parser.parse_args()
    main()
