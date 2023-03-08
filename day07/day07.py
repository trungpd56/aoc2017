#!/usr/bin/env python3
from collections import defaultdict


def cal(t):
    if len(info[t]) == 0:
        return weight[t]
    return weight[t] + sum(weight[i] for i in info[t])


with open('input.txt', 'r') as f:
    lines = f.readlines()

info = defaultdict(list)
weight = defaultdict(int)
child = set()
for line in lines:
    line = line.strip()
    toks = line.split()
    weight[toks[0]] = int(toks[1].strip('()'))
    if '->' in line:
        part = line.strip().split(' -> ')
        c = part[1].split(', ')
        info[toks[0]].extend(c)
        child.update(c)
    else:
        info[toks[0]] = []


part1 = [k for k in info if k not in child][0]
print(f'Part1: {part1}')

part2 = ""
print(f'Part2: {part2}')
