#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import product


def cal(r, c):
    val = 0
    for dr, dc in product((-1, 0, 1), repeat=2):
        if dr == dc == 0:
            continue
        val += nums[(r + dr, c + dc)]
    return val


with open(sys.argv[1], "r") as f:
    num = int(f.read())

res: list[tuple[int, int]] = [(0, 0)]
left, bot = 0, 0
right, top = 1, -1
nums = defaultdict(int)
nums[(0, 0)] = 1
part2 = None
while len(res) < num:
    # go right
    for i in range(left + 1, right + 1):
        res.append((bot, i))
        nums[(bot, i)] = cal(bot, i)
    left -= 1

    # go top
    for i in range(bot - 1, top - 1, -1):
        res.append((i, right))
        nums[(i, right)] = cal(i, right)
    bot += 1

    # go left
    for i in range(right - 1, left - 1, -1):
        res.append((top, i))
        nums[(top, i)] = cal(top, i)
    right += 1

    # go bot:
    for i in range(top + 1, bot + 1):
        res.append((i, left))
        nums[(i, left)] = cal(i, left)
    top -= 1

    for v in nums.values():
        if v > num and part2 is None:
            part2 = v


r, c = res[num - 1]
part1 = abs(r) + abs(c)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

