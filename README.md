# Use cases

* debugging without recompilation
* low-overhead execution profiling

# Example

```bash
git clone https://github.com/bieganski/trace-no-bcc && cd trace-no-bcc

# Trace all PIDs calling function `malloc` from standard C library
sudo ./ftrace.py user /lib/x86_64-linux-gnu/libc.so.6 malloc
```

```
[PID,TID]        [library:symbol]   info
[2757970,2757970][libc.so.6:malloc] REENTRY after 0.0003231 seconds di=0x18, si=0x578612b12010, dx=0xa, cx=0x578619310e38, r8=0x5786193473d0, r9=0x7434841cd3e0, r10=0x578618e959a0
[2757970,2757970][libc.so.6:malloc] RET (ax=0x5786193473d0) exec_time_ns: 0.0000015 seconds
[3212955,3212955][libc.so.6:malloc] REENTRY after 0.0000060 seconds di=0x18, si=0x18, dx=0x18, cx=0x7717283147e2, r8=0x7717283d1460, r9=0x7ffc2beda170, r10=0x0
[3212955,3212955][libc.so.6:malloc] RET (ax=0x5a0fd5ad36e0) exec_time_ns: 0.0000017 seconds
[3212955,3212955][libc.so.6:malloc] REENTRY after 0.0000145 seconds di=0x271, si=0xa, dx=0x34, cx=0x22062041, r8=0x1999999999999999, r9=0x26f, r10=0x271
[3212955,3212955][libc.so.6:malloc] RET (ax=0x5a0fd5ad7e10) exec_time_ns: 0.0000017 seconds
[3212955,3212955][libc.so.6:malloc] REENTRY after 0.0000061 seconds di=0x23, si=0x23, dx=0x23, cx=0x7717283147e2, r8=0x7717283d1460, r9=0x7ffc2beda170, r10=0x0
...
```


```bash
# Trace all invocations of kernel function __x64_sys_mount (see /proc/kallsyms)
 sudo ./ftrace.py kernel __x64_sys_mount
```

```
[1715601,1715601][<kernel>:__x64_sys_mount] FIRST ENTRY di=0xffffb851470dff58, si=0xa5, dx=0x0, cx=0x0, r8=0x0, r9=0x0, r10=0x0
[1715601,1715601][<kernel>:__x64_sys_mount] RET (ax=0xfffffffffffffffe) exec_time_ns: 0.0000153 seconds
[1715604,1715604][<kernel>:__x64_sys_mount] FIRST ENTRY di=0xffffb85147117f58, si=0xa5, dx=0x0, cx=0x0, r8=0x0, r9=0x0, r10=0x0
[1715604,1715604][<kernel>:__x64_sys_mount] RET (ax=0xfffffffffffffffe) exec_time_ns: 0.0000164 seconds
```

# Features

* **userspace code tracing** (either by symbol name or file offset)
* **kernel code tracing** (either by symbol name or kernel virtual memory address)
* [userspace] tracing either shared library code or executable directly
* [userspace] filtering userspace tracee by PID or tracing all PIDs system-wide
* multi-arch, easily extensible



# But.. What if the code that I need to trace is not a global symbol, or is in the middle of a function?

In that case instead of specifying symbol name as an argument, you can pass file offset in hex. In my case, configuration `/lib/x86_64-linux-gnu/libc.so.6 malloc` is equivalent to `/lib/x86_64-linux-gnu/libc.so.6 0xa50a0`, as `0xa50a0` is the file offset (inside an ELF) to the first instruction of `malloc` function:

```bash
m.bieganski@hostname:~$ nm -D  /lib/x86_64-linux-gnu/libc.so.6  | grep "T malloc"
00000000000a50a0 T malloc@@GLIBC_2.2.5
```

How can you get detailed information of function-file offset mapping? Either use `objdump -Fd`, or better try [dwarfseeker](https://github.com/bieganski/dwarfseeker/) (the latter will tell you even inline expansions! Just keep in mind that it requires debug symbols present).


# Runtime requirements
* Linux kernel compiled with CONFIG_BPF_SYSCALL=y (almost certainly true)
* CPython (almost certainly you have it)
* libbpf, v1.4.0 or higher. Either install via `apt-get`-like, or use one ([shipped by us](./libbpf/x86_64/libbpf.so.1)) (latter is default, we download it from `rpmfind.net` using [dload_libbpf.sh](./dload_libbpf.sh))

# Runtime non-requirements :)
* No `requirements.txt` - only Python standard libraries
* No BCC, no libbcc
* No LLVM, no Clang*

`*` - actually optionally it can be used, see [Blob paranoid](#blob-paranoid) section.

# Supported CPU architectures
* x86_64 (64 bit)
* armv7l (32 bit)
* RISC-V (64 bit)

# Distribution
* we are bound by `libbpf`'s license, so it's `LGPL-2.1 OR BSD-2-Clause`.

# Complementary tools
* [lib_get_pub_funcs.sh](./lib_get_pub_funcs.sh) - prints all function names that given shared library exposes. sample use case: `sudo ./ftrace.py user path/to/lib.so $(./lib_get_pub_funcs.sh path/to/lib.so)`

# Blob paranoid?

Under the hood `sudo ftrace.py` loads `uprobe.bpf.o` into your kernel. For full transparency, use [build_bpf.sh](./build_bpf.sh) in order to build `uprobe.bpf.o` from [uprobe.bpf.c](./uprobe.bpf.c). Requires `clang` and `llvm` packages.