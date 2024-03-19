#!/usr/bin/env python3

import sys


def solve(nums: list[int], p2: bool = False) -> int:
    prev, next = 0, 0
    step = 0
    while next < len(nums):
        step += 1
        next += nums[next]
        if not p2:
            nums[prev] += 1
        else:
            nums[prev] += 1 if nums[prev] < 3 else -1
        prev = next
    return step


with open(sys.argv[1], "r") as f:
    nums = [int(l) for l in f.readlines()]

part1 = solve(nums.copy())
print(f"Part 1: {part1}")

part2 = solve(nums, p2=True)
print(f"Part 2: {part2}")

