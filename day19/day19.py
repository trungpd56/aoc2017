#!/usr/bin/env python3

import sys
from collections import defaultdict
from string import ascii_uppercase as uc


class Packet:
    def __init__(self, lines: list[str]) -> None:
        self.dr = 1
        self.dc = 0
        self.sr = 0
        self.grid = defaultdict(lambda: " ")
        for r, line in enumerate(lines):
            for c, ch in enumerate(line.strip("\n")):
                if ch != " ":
                    if r == 0:
                        self.sc = c
                    self.grid[(r, c)] = ch
        self.res = ""
        self.step = 0

    def run(self):
        while True:
            self.step += 1
            cur = self.grid[(self.sr, self.sc)]
            if cur in uc:
                self.res += cur
            elif cur == "+":
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if self.dr + dr == 0 and self.dc + dc == 0:
                        continue
                    ch = self.grid[(self.sr + dr, self.sc + dc)]
                    if ch != " ":
                        self.dr = dr
                        self.dc = dc
                        break
            self.sr += self.dr
            self.sc += self.dc
            if self.grid[(self.sr, self.sc)] == " ":
                return self.res, self.step


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

packet = Packet(lines)

part1, part2 = packet.run()
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

