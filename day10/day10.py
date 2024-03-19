#!/usr/bin/env python3

import sys
from functools import reduce


def knot(seqs: list, n: int = 1) -> list:
    # return list of 256 number with maximum value is 255
    nums = list(range(256))
    skip = 0
    mem = 0
    for _ in range(n):
        for s in seqs:
            nums = nums[:s][::-1] + nums[s:]
            j = (s + skip) % 256
            nums = nums[j:] + nums[:j]
            skip += 1
            mem = (mem + j) % 256
    return nums[-mem:] + nums[:-mem]


with open(sys.argv[1], "r") as f:
    line = f.read().strip()
    seqs = [int(n) for n in line.split(",")]

res = knot(seqs)
part1 = res[0] * res[1]
print(f"Part 1: {part1}")

seqs = [ord(c) for c in line] + [17, 31, 73, 47, 23]
res = knot(seqs, 64)
part2 = ""
for p in zip(*(iter(res),) * 16):
    r = reduce(lambda x, y: x ^ y, p)
    part2 += f"{r:02x}"
print(f"Part 2: {part2}")

