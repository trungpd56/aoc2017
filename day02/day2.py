#!/usr/bin/env python3

import sys
from itertools import combinations

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

part1 = 0
part2 = 0
for line in lines:
    nums = [*map(int, line.split())]
    part1 += max(nums) - min(nums)
    for c in combinations(nums, 2):
        n1, n2 = sorted(c)
        if n2 % n1 == 0:
            part2 += n2 // n1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

