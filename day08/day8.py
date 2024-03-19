#!/usr/bin/env python3

import sys
from collections import defaultdict


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

regs = defaultdict(int)
part2 = 0
for line in lines:
    line = line.replace('inc', '+=').replace('dec', '-=')
    t = line.strip().split()
    sm = f"if regs['{t[4]}'] {' '.join(t[5:])}: regs['{t[0]}'] {t[1]} {t[2]}"
    # this is not recommended, just want to hack a bit
    exec(sm)
    part2 = max(part2, *regs.values())

part1 = max(regs.values())
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
