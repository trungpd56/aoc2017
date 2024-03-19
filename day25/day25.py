#!/usr/bin/env python3

import sys


class State:
    def __init__(self, lines: list[str]) -> None:
        self.name = lines[0].split()[-1].strip(":")
        self.val0 = 1 if lines[2].split()[-1] == "1." else 0
        self.pos0 = -1 if lines[3].split()[-1] == "left." else 1
        self.next0 = lines[4].split()[-1].strip(".")
        self.val1 = 1 if lines[6].split()[-1] == "1." else 0
        self.pos1 = -1 if lines[7].split()[-1] == "left." else 1
        self.next1 = lines[8].split()[-1].strip(".")

    def __repr__(self) -> str:
        return f"<State {self.__dict__}>"


with open(sys.argv[1], "r") as f:
    raws = f.read().split("\n\n")

ss = {}
total = int(raws[0].split()[-2])
for lines in raws[1:]:
    s = State(lines.splitlines())
    ss[s.name] = s


res = set()
pos = 0
s = ss["A"]
next = ""
cnt = 0
while (cnt := cnt + 1) <= total:
    # cur = 0 if not in res
    if pos not in res:
        if s.val0:
            res.add(pos)
        pos += s.pos0
        next = s.next0
    # cur = 1
    else:
        if not s.val1:
            res.remove(pos)
        pos += s.pos1
        next = s.next1
    s = ss[next]
    print(f"\rTotal: {len(res):>5d}", end="")

print()
part1 = len(res)
print(f"Part 1: {part1}")

