#!/usr/bin/env python3

import sys
from string import ascii_lowercase as lc


class Prog:
    def __init__(self, line: str, p: str = lc[:16]) -> None:
        self.p = p
        self.lines = line.strip().split(",")

    def spin(self, x: int):
        x = -x
        self.p = self.p[x:] + self.p[:x]

    def exchange(self, nx: int, ny: int):
        nx, ny = sorted((nx, ny))
        self.p = (
            self.p[:nx]
            + self.p[ny]
            + self.p[nx + 1 : ny]
            + self.p[nx]
            + self.p[ny + 1 :]
        )

    def partner(self, x: str, y: str):
        nx, ny = self.p.index(x), self.p.index(y)
        self.exchange(nx, ny)

    def run(self):
        for line in self.lines:
            match line[0]:
                case "s":
                    self.spin(int(line[1:]))
                case "x":
                    n1, n2 = map(int, line[1:].split("/"))
                    self.exchange(n1, n2)
                case "p":
                    x, y = line[1:].split("/")
                    self.partner(x, y)
        return self.p


with open(sys.argv[1], "r") as f:
    line = f.read()

seen = []
prog = Prog(line)
i = 0
while True:
    print(i)
    r = prog.run()
    if r in seen:
        break
    seen.append(r)
    i += 1

part1 = seen[0]
print(f"Part 1: {part1}")

part2 = 1_000_000_000 % i - 1
part2 = seen[part2]
print(f"Part 2: {part2}")

