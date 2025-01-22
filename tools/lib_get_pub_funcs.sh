#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "usage: $0 <executable/library path>"
    exit 1
fi

LIB=$1

nm -D $LIB | grep " T " | awk '{ print $3 }' | cut -d @ -f 1 | paste -s -d ' '


