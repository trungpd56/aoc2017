#!/usr/bin/env python3

import sys
from typing import Generator


def gen(val: int, factor: int) -> Generator:
    while True:
        val = val * factor % 2147483647
        yield val


def gen2(val: int, factor: int, mod: int) -> Generator:
    while True:
        val = val * factor % 2147483647
        if val % mod == 0:
            yield val


def solve(ga: Generator, gb: Generator, num: int) -> int:
    res = 0
    for i, (a, b) in enumerate(zip(ga, gb)):
        if bin(a)[-16:] == bin(b)[-16:]:
            res += 1
        if i == num - 1:
            break
    return res


with open(sys.argv[1], "r") as f:
    numa, numb = [int(l.split()[-1]) for l in f.readlines()]

gena = gen(numa, 16807)
genb = gen(numb, 48271)
part1 = solve(gena, genb, 40_000_000)
print(f"Part 1: {part1}")

gena = gen2(numa, 16807, 4)
genb = gen2(numb, 48271, 8)
part2 = solve(gena, genb, 5_000_000)
print(f"Part 2: {part2}")

