#!/usr/bin/env python3

import sys
from collections import deque


def solve(queue: deque) -> tuple[int, int]:
    res = []
    score = 0
    cnt = 0
    while queue:
        c = queue.popleft()
        if c == "<":
            while (j := queue.popleft()) != ">":
                if j == "!":
                    queue.popleft()
                    continue
                cnt += 1
        elif c == "{":
            res.append(c)
        elif c == "}":
            score += len(res)
            res.pop()
    return score, cnt


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

part1 = 0
part2 = 0
for line in lines:
    q = deque(line.strip())
    s, c = solve(q)
    part1 += s
    part2 += c

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

