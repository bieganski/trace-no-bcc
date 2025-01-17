#!/bin/bash

set -eu

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
DEST_DIR=$SCRIPT_DIR/libbpf

ARCH_CHOICES=(x86_64 riscv64)
URLS=( \
https://fr.rpmfind.net/linux/centos-stream/9-stream/BaseOS/x86_64/os/Packages/libbpf-1.4.0-1.el9.x86_64.rpm
https://fr.rpmfind.net/linux/opensuse/ports/riscv/tumbleweed/repo/oss/riscv64/libbpf1-1.5.0-2.1.riscv64.rpm 
)

for (( i=0; i<${#ARCH_CHOICES[*]}; ++i)); do
    arch=${ARCH_CHOICES[$i]}
    url=${URLS[$i]}
    mkdir -p $DEST_DIR/$arch/
    pushd $DEST_DIR/$arch/ > /dev/null
    curl -o libbpf.rpm $url
    version=`basename $url | cut -d - -f 2 | cut -d . -f 1,2`.0
    rpm2cpio libbpf.rpm | cpio -iv --to-stdout ./usr/lib64/libbpf.so.$version > libbpf.so.1
    rm libbpf.rpm
    popd > /dev/null
done