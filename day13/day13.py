#!/usr/bin/env python3
from collections import defaultdict


def slot_position(t, length):
    period = 2 * (length - 1)
    pos = t % period
    if pos >= length:
        pos = 2 * (length - 1) - pos
    return pos % length


with open('input.txt', 'r') as f:
    lines = f.readlines()

layer = defaultdict(int)
for line in lines:
    toks = line.strip().split(': ')
    layer[int(toks[0])] = int(toks[1])

pos = (-1, 0)
sv = []
for t in range(max(layer)+1):
    fw = []
    pos = (pos[0]+1, 0)
    for n, length in layer.items():
        y = slot_position(t, length)
        fw.append((n, y))
    if pos in fw:
        sv.append((pos[0], layer[pos[0]]))

part1 = sum(x*y for x, y in sv)
print(f'Part1: {part1}')

part2 = ""
print(f'Part2: {part2}')
