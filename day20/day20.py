#!/usr/bin/env python3

import re
import sys
from dataclasses import dataclass


@dataclass
class Particle:
    num: int
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int
    ax: int
    ay: int
    az: int

    def step(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    @property
    def score(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def collide(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

ps = []
for i, line in enumerate(lines):
    ps.append(Particle(i, *map(int, re.findall(r"-?\d+", line))))


minr = float("inf")
cnt = 0
while cnt < 1000:
    for p in ps:
        p.step()
    r = min(ps, key=lambda x: x.score)
    if r.score < minr:
        minr = r.score
        cnt = 0
    else:
        cnt += 1
part1 = r.num
print(f"Part 1: {part1}")

ps = []
for i, line in enumerate(lines):
    ps.append(Particle(i, *map(int, re.findall(r"-?\d+", line))))

cnt = 0
total = 0
while cnt < 10:
    remove = []
    for p in ps:
        p.step()
    for p1 in ps:
        for p2 in ps:
            if p1 is p2:
                continue
            if p1.collide(p2):
                remove.extend([p1, p2])
    ps = [p for p in ps if p not in remove]
    if len(ps) != total:
        total = len(ps)
        cnt = 0
    else:
        cnt += 1
part2 = total
print(f"Part 2: {part2}")

