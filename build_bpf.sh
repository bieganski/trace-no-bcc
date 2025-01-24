#!/bin/bash

set -e

clang -g -O2 -Wall -target bpf -c uprobe.bpf.c -o uprobe.bpf.o
llvm-strip -g uprobe.bpf.o
echo "uprobe.bpf.o OK"