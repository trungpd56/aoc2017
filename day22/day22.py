#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    lines = [l.strip() for l in f.readlines()]

size = len(lines) // 2
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

grid = {
    (r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == "#"
}
sr, sc = size, size
d = 0
part1 = 0
for _ in range(10000):
    val = 1 if (sr, sc) in grid else -1
    d = (d + val) % 4
    if (sr, sc) not in grid:
        grid.add((sr, sc))
        part1 += 1
    else:
        grid.remove((sr, sc))
    dr, dc = dirs[d]
    sr, sc = sr + dr, sc + dc
print(f"Part 1: {part1}")

grid = defaultdict(lambda: ".")
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        grid[(r, c)] = ch

sr, sc = size, size
d = 0
part2 = 0
for _ in range(10000000):
    match grid[(sr, sc)]:
        case "W":
            val = 0
            state = "#"
            part2 += 1
        case "#":
            val = 1
            state = "F"
        case "F":
            val = 2
            state = "."
        case ".":
            val = -1
            state = "W"
        case _:
            assert False
    d = (d + val) % 4
    grid[(sr, sc)] = state
    dr, dc = dirs[d]
    sr, sc = sr + dr, sc + dc
print(f"Part 2: {part2}")

