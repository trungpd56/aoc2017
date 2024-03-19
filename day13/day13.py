#!/usr/bin/env python3

import sys
from collections import defaultdict


def solve(delay: int) -> tuple[int, bool]:
    severity = 0
    caught = False
    for k, v in layers.items():
        if v == 0:
            continue
        if (k + delay) % (2 * (v - 1)) == 0:
            severity += k * v
            caught = True
    return severity, caught


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

layers = defaultdict(int)
for line in lines:
    n1, n2 = map(int, line.split(": "))
    layers[n1] = n2

part1 = solve(0)[0]
print(f"Part 1: {part1}")

part2 = 0
while solve(part2)[1]:
    part2 += 1
print(f"Part 2: {part2}")
