#!/usr/bin/env python3

import sys
from collections import defaultdict
from typing import Iterator

pattern = ".#.\n..#\n###"
pat = pattern.splitlines()


def gen(pat: list[str]) -> Iterator[str]:
    # rotate left
    for _ in range(4):
        pat = list(zip(*pat))[::-1]
        # yield rotate
        yield "/".join(map("".join, pat))
        # yield flip
        yield "/".join(map("".join, [l[::-1] for l in pat]))


def enhance(pat: list[str]) -> list[str]:
    for g in gen(pat):
        if g in info:
            break
    return info[g].split("/")


def solve(pat: list[str], n: int):
    res = []
    # seperate by n row
    for rows in zip(*(iter(pat),) * n):
        cols = list(zip(*rows))
        # seperate by n col
        for col in zip(*(iter(cols),) * n):
            res.append(enhance(list(zip(*col))))

    return res


def combine(pat: list[list[str]], n: int) -> list[str]:
    res = []
    for rows in zip(*(iter(pat),) * n):
        for r in zip(*rows):
            res.append("".join(r))
    return res


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

info = defaultdict(str)
for line in lines:
    k, v = line.strip().split(" => ")
    info[k] = v

for t in range(18):
    size = len(pat)
    if size % 2 == 0:
        pat = solve(pat, 2)
        pat = combine(pat, size // 2)
    else:
        pat = solve(pat, 3)
        pat = combine(pat, size // 3)
    if t == 4:
        part1 = sum([line.count("#") for line in pat])


print(f"Part 1: {part1}")
part2 = sum([line.count("#") for line in pat])
print(f"Part 2: {part2}")
