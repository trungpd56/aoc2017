#!/usr/bin/env python3

import sys


def solve(line: str, p2: bool = False) -> bool:
    t = line.split()
    if p2:
        t = ["".join(sorted(w)) for w in t]
    return len(t) == len(set(t))


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

part1 = 0
part2 = 0
for line in lines:
    part1 += solve(line)
    part2 += solve(line, True)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

