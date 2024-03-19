#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    nums = [int(t) for t in f.read().split()]

# nums = [0, 2, 7, 0]
seen = set()
part1 = None
line = ""
step = 0
while True:
    if str(nums) in seen:
        if not part1:
            part1 = step
            line = str(nums)
        else:
            if line == str(nums):
                part2 = step - part1
                break
    seen.add(str(nums))
    mnum = max(nums)
    i = nums.index(mnum)
    nums[i] = 0
    for _ in range(mnum):
        nums[(i + 1) % len(nums)] += 1
        i += 1
    step += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

