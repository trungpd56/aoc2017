#!/usr/bin/env python3

import sys


def dfs(l, next, p2: bool = False):
    total = sum(l[-1])
    maxl = 0
    maxv = 0
    for p in paths:
        if 0 in p:
            continue
        if next in p and p not in l:
            i = p.index(next)
            v, length = dfs(l + [p], p[1 - i], p2)
            if not p2:
                maxv = max(maxv, v)
            else:
                if length >= maxl:
                    maxl = length
                    maxv = max(maxv, v)
    total += maxv
    return total, 1 + maxl


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

paths = [tuple(map(int, l.split("/"))) for l in lines]

part1 = max(dfs([p], p[1 - p.index(0)]) for p in paths if 0 in p)[0]
print(f"Part 1: {part1}")

part2 = max(dfs([p], p[1 - p.index(0)], p2=True) for p in paths if 0 in p)[0]
print(f"Part 2: {part2}")

