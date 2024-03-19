#!/usr/bin/env python3

import sys
from collections import defaultdict
from queue import Empty, Queue
from threading import Thread


class Comp:
    def __init__(self, lines: list[str], p=0, iq=None, oq=None) -> None:
        self.lines = [l.strip() for l in lines]
        self.regs = defaultdict(int)
        self.regs["p"] = p
        self.sound: int = 0
        self.iq = iq
        self.oq = oq
        self.cnt = 0

    def get(self, x):
        try:
            return int(x)
        except ValueError:
            return self.regs[x]

    def rcv(self, x):
        if self.iq is None:
            return self.sound if self.get(x) != 0 else None
        else:
            try:
                self.regs[x] = self.iq.get(timeout=5)
            except Empty:
                return self.cnt

    def snd(self, x):
        if self.iq is None:
            self.sound = self.get(x)
        else:
            self.oq.put(self.get(x))
            self.cnt += 1

    def run(self):
        eip = 0
        while 0 <= eip < len(self.lines):
            t = self.lines[eip].split()
            match t[0]:
                case "snd":
                    self.snd(t[1])
                case "set":
                    self.regs[t[1]] = self.get(t[2])
                case "add":
                    self.regs[t[1]] += self.get(t[2])
                case "mul":
                    self.regs[t[1]] *= self.get(t[2])
                case "mod":
                    self.regs[t[1]] %= self.get(t[2])
                case "rcv":
                    if (r := self.rcv(t[1])) is not None:
                        return r
                case "jgz":
                    eip += self.get(t[2]) if self.get(t[1]) > 0 else 1
                    continue
                case _:
                    assert False
            eip += 1


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

comp = Comp(lines)
part1 = comp.run()
print(f"Part 1: {part1}")

q0 = Queue()
q1 = Queue()
c0 = Comp(lines, 0, q0, q1)
c1 = Comp(lines, 1, q1, q0)
t0 = Thread(target=c0.run)
t1 = Thread(target=c1.run)
t0.start()
t1.start()
t0.join()
t1.join()
part2 = c1.cnt
print(f"Part 2: {part2}")

