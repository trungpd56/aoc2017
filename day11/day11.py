#!/usr/bin/env python3

import sys

dirs = {
    "n": (0, 1, -1),
    "ne": (1, 0, -1),
    "nw": (-1, 1, 0),
    "s": (0, -1, 1),
    "se": (1, -1, 0),
    "sw": (-1, 0, 1),
}

with open(sys.argv[1], "r") as f:
    line = f.read().strip()

x, y, z = 0, 0, 0
part2 = 0
for c in line.split(","):
    dx, dy, dz = dirs[c]
    x += dx
    y += dy
    z += dz
    dist = (abs(x) + abs(y) + abs(z)) // 2
    part2 = max(part2, dist)

part1 = (abs(x) + abs(y) + abs(z)) // 2
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
