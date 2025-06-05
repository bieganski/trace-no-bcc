#include <stdint.h>

// for better portability we don't include from libbpf-dev, instead copy-paste relevant pieces.
//
//
// #include <linux/bpf.h>
// #include <bpf/bpf_helpers.h>
// #include "vmlinux.h"


#define __VMLINUX_H__

#define __uint(name, val) int (*name)[val]

#define __u64 uint64_t
#define __u32 uint32_t
#define __u16 uint16_t
#define __s64 int64_t
#define __s32 int32_t
#define __be16 __u16 
#define __be32 __u32
#define __wsum __u32
#define BPF_MAP_TYPE_RINGBUF 27

#define BPF_PRINTK_FMT_MOD static const

#define ___bpf_nth(_, _1, _2, _3, _4, _5, _6, _7, _8, _9, _a, _b, _c, N, ...) N

#define ___bpf_narg(...) \
	___bpf_nth(_, ##__VA_ARGS__, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

#define __bpf_vprintk(fmt, args...)				\
({								\
	static const char ___fmt[] = fmt;			\
	unsigned long long ___param[___bpf_narg(args)];		\
								\
	_Pragma("GCC diagnostic push")				\
	_Pragma("GCC diagnostic ignored \"-Wint-conversion\"")	\
	___bpf_fill(___param, args);				\
	_Pragma("GCC diagnostic pop")				\
								\
	bpf_trace_vprintk(___fmt, sizeof(___fmt),		\
			  ___param, sizeof(___param));		\
})

#define __bpf_printk(fmt, ...)				\
({							\
	BPF_PRINTK_FMT_MOD char ____fmt[] = fmt;	\
	bpf_trace_printk(____fmt, sizeof(____fmt),	\
			 ##__VA_ARGS__);		\
})

#define ___bpf_pick_printk(...) \
	___bpf_nth(_, ##__VA_ARGS__, __bpf_vprintk, __bpf_vprintk, __bpf_vprintk,	\
		   __bpf_vprintk, __bpf_vprintk, __bpf_vprintk, __bpf_vprintk,		\
		   __bpf_vprintk, __bpf_vprintk, __bpf_printk /*3*/, __bpf_printk /*2*/,\
		   __bpf_printk /*1*/, __bpf_printk /*0*/)

/* Helper macro to print out debug messages */
#define bpf_printk(fmt, args...) ___bpf_pick_printk(args)(fmt, ##args)


static void (*bpf_ringbuf_submit)(void *data, __u64 flags) = (void *) 132;
static __u64 (*bpf_get_current_pid_tgid)(void) = (void *) 14;
static long (*bpf_probe_read_kernel_str)(void *dst, __u32 size, const void *unsafe_ptr) = (void *) 115;
static __u64 (*bpf_ktime_get_ns)(void) = (void *) 5;
static void *(*bpf_ringbuf_reserve)(void *ringbuf, __u64 size, __u64 flags) = (void *) 131;
static long (*bpf_trace_printk)(const char *fmt, __u32 fmt_size, ...) = (void *) 6;

struct pt_regs_x86_64 {
        unsigned long r15;
        unsigned long r14;
        unsigned long r13;
        unsigned long r12;
        unsigned long bp;
        unsigned long bx;
        unsigned long r11;
        unsigned long r10;
        unsigned long r9;
        unsigned long r8;
        unsigned long ax;
        unsigned long cx;
        unsigned long dx;
        unsigned long si;
        unsigned long di;
        unsigned long orig_ax;
        unsigned long ip;
        unsigned long cs;
        unsigned long flags;
        unsigned long sp;
        unsigned long ss;
};

struct pt_regs_riscv64 {
	long unsigned int epc;
	long unsigned int ra;
	long unsigned int sp;
	long unsigned int gp;
	long unsigned int tp;
	long unsigned int t0;
	long unsigned int t1;
	long unsigned int t2;
	long unsigned int s0;
	long unsigned int s1;
	long unsigned int a0;
	long unsigned int a1;
	long unsigned int a2;
	long unsigned int a3;
	long unsigned int a4;
	long unsigned int a5;
	long unsigned int a6;
	long unsigned int a7;
	long unsigned int s2;
	long unsigned int s3;
	long unsigned int s4;
	long unsigned int s5;
	long unsigned int s6;
	long unsigned int s7;
	long unsigned int s8;
	long unsigned int s9;
	long unsigned int s10;
	long unsigned int s11;
	long unsigned int t3;
	long unsigned int t4;
	long unsigned int t5;
	long unsigned int t6;
	long unsigned int status;
	long unsigned int badaddr;
	long unsigned int cause;
	long unsigned int orig_a0;
};

struct pt_regs_armv7l {
	uint32_t uregs[18];
};

#define SEC(name) \
	_Pragma("GCC diagnostic push")					    \
	_Pragma("GCC diagnostic ignored \"-Wignored-attributes\"")	    \
	__attribute__((section(name), used))				    \
	_Pragma("GCC diagnostic pop")					    \




// ---------------  PROGRAM LOGIC BEGIN

SEC(".data.symbol_name") static char symbol_name[64] = "MOCK_SYMBOL";
SEC(".data.library_path") static char library_path[128] = "MOCK_LIBRARY";

// NOTE: setting all arch to 0 here and setting only one at 1 at load time would be easier,
// but we need to prevent dead code elimination by clang now.
SEC(".rodata.arch_is_x86_64") static volatile const uint32_t arch_is_x86_64 = 1;
SEC(".rodata.arch_is_riscv64") static volatile const uint32_t arch_is_riscv64 = 1;
SEC(".rodata.arch_is_armv7l") static volatile const uint32_t arch_is_armv7l = 1;

char LICENSE[] SEC("license") = "Dual BSD/GPL";

struct {
	__uint(type, BPF_MAP_TYPE_RINGBUF);
	__uint(max_entries, 256 * 1024 /* 256 KB */);
} rb SEC(".maps");

struct event {
	char library_path[128];
	char symbol_name[64];
	int32_t pid;
	int32_t tid;

	uint64_t timestamp;
	int32_t is_ret;

	union {
		struct pt_regs_x86_64  regs_x86_64;
		struct pt_regs_riscv64 regs_riscv64;
		struct pt_regs_armv7l  regs_armv7l;
	};
};

__always_inline static void copy_pid_tid(struct event* e) {
	uint64_t pid_tid = bpf_get_current_pid_tgid();
	int pid = pid_tid >> 32;
	int tid = (uint32_t) pid_tid;
	e->pid = pid;
	e->tid = tid;
}

__always_inline static void copy_regs(void* regs, struct event* e) {
	int copied = 0;

	if (arch_is_armv7l) {
		e->regs_armv7l = *(struct pt_regs_armv7l*) regs;
		copied = 1;
	} 
	
	if (arch_is_riscv64) {
		e->regs_riscv64 = *(struct pt_regs_riscv64*) regs;
		copied = 1;
	} 
	
	if (arch_is_x86_64) {
		e->regs_x86_64 = *(struct pt_regs_x86_64*) regs;
		copied = 1;
	} 
	
	if (!copied) {
		bpf_printk("runtime arch detection failed: No register copy performed!");
	}
}

SEC("uprobe//")
int uprobe_funcname(void* ctx)
{
	struct event *e = bpf_ringbuf_reserve(&rb, sizeof(*e), 0);
	if (!e)
		return 0;

	e->is_ret = 0;
	e->timestamp = bpf_ktime_get_ns();
	bpf_probe_read_kernel_str(e->library_path, 128, library_path);
	bpf_probe_read_kernel_str(e->symbol_name, 64, symbol_name);
	copy_pid_tid(e);
	copy_regs(ctx, e);

	bpf_ringbuf_submit(e, 0);

	return 0;
}

SEC("uprobe//")
int ret_uprobe_funcname(void* ctx)
{
	struct event *e = bpf_ringbuf_reserve(&rb, sizeof(*e), 0);
	if (!e)
		return 0;

	e->is_ret = 1;
	e->timestamp = bpf_ktime_get_ns();
	bpf_probe_read_kernel_str(e->library_path, 128, library_path);
	bpf_probe_read_kernel_str(e->symbol_name, 64, symbol_name);
	copy_pid_tid(e);
	copy_regs(ctx, e);

	bpf_ringbuf_submit(e, 0);

	return 0;
}
