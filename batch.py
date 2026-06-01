from pathlib import Path
from asstrace import API

import gen2.bpf as bpf
# raise ValueError(bpf.BPF_PROG_LOAD)

import ctypes
import time
from inspect import getmembers
from pprint import pformat

x = lambda _y: pformat(getmembers(_y))

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

import os
print("PID: ", os.getpid())
bpf_prog_load__bpf_attr = bpf.struct_anon_17

# defining function called asstrace_X will make a hook for syscall named 'X'.
# hook will be executed before each entry to 'X'.
def asstrace_bpf(op, ptr, *_):
    # print("AAA ", op, hex(ptr), "SLEEP")
    mem = API.ptrace_read_mem(address=ptr, size=152)
    attr = bpf_prog_load__bpf_attr.from_buffer_copy(mem)
    if attr.prog_type == bpf.BPF_PROG_TYPE_KPROBE and b"uprobe" in attr.prog_name and b"ret" in attr.prog_name:
        # raise ValueError(hex(attr.insns))
        instructions = API.ptrace_read_mem(address=attr.insns, size=8 * attr.insn_cnt) 
        print(f"size: {attr.insn_cnt}", [hex(int.from_bytes(x,"big")) for x in chunks(instructions, 8)])
        raise ValueError("DONER")
    API.invoke_syscall_anyway()
    return