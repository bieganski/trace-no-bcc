#!/usr/bin/env python3

import subprocess
from pathlib import Path
import logging
from enum import Enum

logging.basicConfig(level=logging.INFO)

class bcolors(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    GREEN_DARK = '\033[32m'
    ORANGE = '\033[33m'
    WHITE = '\033[97m'


def run_shell(cmd: str) -> tuple[str, str]:
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
    stdout, stderr = process.communicate()
    if (ecode := process.returncode):
        raise ValueError(f"Command <{cmd}> exited with {ecode}")
    return stdout, stderr

def bpf_helper_map() -> dict[str, int]:
    import json
    j = Path(__file__).parent / "gen" / "bpf_helpers.json"
    return json.loads(j.read_text())    


def main(path: Path):
    content = path.read_text()
    map : dict[str, int] = bpf_helper_map()
    rmap = {v: k for k, v in map.items()}
    lines = content.splitlines()

    for i, line in enumerate(lines):
        if "\tcall" in line:
            num_str = line.split()[-1]
            base = 16 if num_str.startswith("0x") else 10
            num = int(num_str, base)
            lines[i] = f"{line} ({bcolors.OKCYAN.value}{rmap[num]}{bcolors.ENDC.value})"
    print("\n".join(lines))

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(usage="XXX")
    parser.add_argument("path", nargs="?", type=Path, default=Path("/dev/stdin"))
    main(**vars(parser.parse_args()))
