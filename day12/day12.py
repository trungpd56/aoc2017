#!/usr/bin/env python3

import re
import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

path = defaultdict(list)
for line in lines:
    k, *v = map(int, re.findall(r"\d+", line))
    path[k] = v

seen = set()


def dfs(p: int) -> int:
    if p in seen:
        return 0
    seen.add(p)
    return 1 + sum(dfs(i) for i in path[p])


part1 = dfs(0)
print(f"Part 1: {part1}")

part2 = 1
for k in path:
    if k in seen:
        continue
    part2 += 1
    dfs(k)
print(f"Part 2: {part2}")

