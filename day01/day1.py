#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    nums = list(map(int, f.read().strip()))

part1 = 0
for i in range(len(nums)):
    if nums[i] == nums[(i + 1) % len(nums)]:
        part1 += nums[i]
print(f"Part 1: {part1}")

mid = len(nums) // 2
part2 = 0
for n1, n2 in zip(nums[:mid], nums[mid:]):
    if n1 == n2:
        part2 += 2 * n1

print(f"Part 2: {part2}")

