#!/usr/bin/env python3

import sys
from collections import defaultdict


class Comp:
    def __init__(self, lines: list[str]) -> None:
        self.lines = [l.strip() for l in lines]
        self.regs = defaultdict(int)
        self.cnt = 0

    def get(self, x):
        try:
            return int(x)
        except ValueError:
            return self.regs[x]

    def run(self):
        eip = 0
        while 0 <= eip < len(self.lines):
            t = self.lines[eip].split()
            match t[0]:
                case "set":
                    self.regs[t[1]] = self.get(t[2])
                case "sub":
                    self.regs[t[1]] -= self.get(t[2])
                case "mul":
                    self.cnt += 1
                    self.regs[t[1]] *= self.get(t[2])
                case "jnz":
                    eip += self.get(t[2]) if self.get(t[1]) != 0 else 1
                    continue
                case _:
                    assert False, f"{t}"
            eip += 1
        return self.cnt


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# part1
comp = Comp(lines)
part1 = comp.run()
print(f"Part 1: {part1}")

# part2: need to analyze the diagram
b = 109_900
c = 126_900
part2 = 0
for b in range(b, c + 1, 17):
    for i in range(2, b):
        if b % i == 0:
            part2 += 1
            break
print(f"Part 2: {part2}")
