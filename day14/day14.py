#!/usr/bin/env python3

import sys
from functools import reduce


def knot(line: str) -> str:
    # return list of 256 number with maximum value is 255
    seqs = [ord(c) for c in line] + [17, 31, 73, 47, 23]
    nums = list(range(256))
    skip = 0
    mem = 0
    for _ in range(64):
        for s in seqs:
            nums = nums[:s][::-1] + nums[s:]
            j = (s + skip) % 256
            nums = nums[j:] + nums[:j]
            skip += 1
            mem = (mem + j) % 256
    tmp = nums[-mem:] + nums[:-mem]
    res = ""
    for p in zip(*(iter(tmp),) * 16):
        r = reduce(lambda x, y: x ^ y, p)
        res += f"{r:08b}"

    return res


with open(sys.argv[1], "r") as f:
    key = f.read().strip()

grid = []
for i in range(128):
    grid.append(knot(f"{key}-{i}"))

part1 = sum(line.count("1") for line in grid)
print(f"Part 1: {part1}")

seen = set()


def dfs(r, c):
    if (r, c) in seen or r < 0 or r >= 128 or c < 0 or c >= 128 or grid[r][c] == "0":
        return
    seen.add((r, c))
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)


part2 = 0
for r in range(128):
    for c in range(128):
        if (r, c) in seen or grid[r][c] == "0":
            continue
        part2 += 1
        dfs(r, c)

print(f"Part 2: {part2}")

