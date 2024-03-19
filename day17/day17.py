#!/usr/bin/env python3

import sys
from collections import deque

with open(sys.argv[1], "r") as f:
    num = int(f.read())

q = deque([0])
for i in range(1, 2018):
    q.rotate(-num)
    q.append(i)

part1 = q[0]
print(f"Part 1: {part1}")

azero = None
cur = 0
for i in range(1, 50000000 + 1):
    cur = (cur + num + 1) % i
    if cur == 0:
        azero = i

part2 = azero
print(f"Part 2: {part2}")
