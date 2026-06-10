from pathlib import Path
from asstrace import API

import gen2.bpf as bpf
import gen2.libbpf as libbpf
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

#  ('_objects', None),
#  ('aux_output', 0),
#  ('aux_sample_size', 0),
#  ('aux_watermark', 0),
#  ('bp_addr', 93824992608928),
#  ('bp_len', 676000),
#  ('bp_type', 0),
#  ('bpf_event', 0),
#  ('branch_sample_type', 0),
#  ('build_id', 0),
#  ('cgroup', 0),
#  ('clockid', 0),
#  ('comm', 0),
#  ('comm_exec', 0),
#  ('config', 0),
#  ('config1', 93824992608928),
#  ('config2', 676000),
#  ('config3', 0),
#  ('context_switch', 0),
#  ('disabled', 0),
#  ('enable_on_exec', 0),
#  ('exclude_callchain_kernel', 0),
#  ('exclude_callchain_user', 0),
#  ('exclude_guest', 0),
#  ('exclude_host', 0),
#  ('exclude_hv', 0),
#  ('exclude_idle', 0),
#  ('exclude_kernel', 0),
#  ('exclude_user', 0),
#  ('exclusive', 0),
#  ('freq', 0),
#  ('inherit', 0),
#  ('inherit_stat', 0),
#  ('inherit_thread', 0),
#  ('kprobe_addr', 676000),
#  ('kprobe_func', 93824992608928),
#  ('ksymbol', 0),
#  ('mmap', 0),
#  ('mmap2', 0),
#  ('mmap_data', 0),
#  ('namespaces', 0),
#  ('pinned', 0),
#  ('precise_ip', 0),
#  ('probe_offset', 676000),
#  ('read_format', 0),
#  ('remove_on_exec', 0),
#  ('sample_freq', 0),
#  ('sample_id_all', 0),
#  ('sample_max_stack', 0),
#  ('sample_period', 0),
#  ('sample_regs_intr', 0),
#  ('sample_regs_user', 0),
#  ('sample_stack_user', 0),
#  ('sample_type', 0),
#  ('sig_data', 0),
#  ('sigtrap', 0),
#  ('size', 136),
#  ('task', 0),
#  ('text_poke', 0),
#  ('type', 9),
#  ('unnamed_perf_event_attr_1',
#   <gen2.libbpf.union_anon_184 object at 0x7ffff729b3c0>),
#  ('unnamed_perf_event_attr_2',
#   <gen2.libbpf.union_anon_185 object at 0x7ffff729b440>),
#  ('unnamed_perf_event_attr_3',
#   <gen2.libbpf.union_anon_186 object at 0x7ffff729a540>),
#  ('unnamed_perf_event_attr_4',
#   <gen2.libbpf.union_anon_187 object at 0x7ffff729b540>),
#  ('uprobe_path', 93824992608928),
#  ('use_clockid', 0),
#  ('wakeup_events', 0),
#  ('wakeup_watermark', 0),
#  ('watermark', 0),
#  ('write_backward', 0)]


def asstrace_perf_event_open(attr_ptr, pid, cpu, group_fd, flags, *_):
    mem = API.ptrace_read_mem(address=attr_ptr, size=0x88)
    attr = libbpf.struct_perf_event_attr.from_buffer_copy(mem)
    # raise ValueError(API.ptrace_read_null_terminated(attr.uprobe_path, 0x100))
    # raise ValueError(attr.probe_offset)
    raise ValueError(x(attr))
