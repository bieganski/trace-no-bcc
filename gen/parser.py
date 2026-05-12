#!/usr/bin/env python3
"""Parse bpf_helper_defs.h and output function name -> ID mapping as JSON."""

import json
import re
import sys
from pathlib import Path


def parse_bpf_helper_defs(filepath: Path) -> dict:
    d = {}
    for line in filepath.read_text().splitlines():
        if not line.startswith("static"):
            continue
        tokens = line.split()
        for t in tokens:
            if ")(" in t:
                func = t.split(")")[0]
                id = tokens[-1][:-1]
                d[func] = int(id)
    for x in range(min(d.values()), max(d.values())):
        if x not in d.values():
            raise ValueError(f"{x} not in values")
    return d


def main():
    filepath = Path(__file__).parent / 'bpf_helper_defs.h'
    
    if len(sys.argv) > 1:
        filepath = Path(sys.argv[1])
    
    if not filepath.exists():
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)
    
    helpers = parse_bpf_helper_defs(filepath)
    print(json.dumps(helpers, indent=2))


if __name__ == '__main__':
    main()
