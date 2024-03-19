#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict


def solve(line: str) -> int:
    if len(path[line]) == 0:
        return val[line]
    total = val[line]
    res = [solve(p) for p in path[line]]
    if len(set(res)) == 1:
        total += sum(res)
        return total
    else:
        mc = Counter(res).most_common()
        assert len(mc) == 2
        n1, n2 = mc
        delta = n1[0] - n2[0]
        node = [p for p in path[line] if solve(p) == n2[0]][0]
        raise ValueError(f"Value must be {val[node]+delta}")


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

val = defaultdict(int)
path = defaultdict(list)
for line in lines:
    ps = line.strip().split(" -> ")
    k, v = ps[0].split()
    val[k] = int(v.strip("()"))
    if len(ps) > 1:
        path[k] = ps[1].split(", ")

part1 = ""
for k in val:
    if all(k not in c for c in path.values()):
        part1 = k
print(f"Part 1: {part1}")

part2 = solve(part1)
print(f"Part 2: {part2}")

