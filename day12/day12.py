#!/usr/bin/env python3
from collections import defaultdict


def walk(visited, dst):
    if visited[-1] == dst:
        # print(visited)
        return True
    return any(walk(visited + [i], dst) for i in info[visited[-1]] if i not in visited)


with open('input.txt', 'r') as f:
    lines = f.readlines()

info = defaultdict(set)
for line in lines:
    part = line.strip().split(' <-> ')
    if ',' in part[1]:
        toks = part[1].split(', ')
        for t in toks:
            info[part[0]].add(t)
            info[t].add(part[0])
    else:
        info[part[0]].add(part[1])
        info[part[1]].add(part[0])


part1 = sum(walk([i], '0') for i in info)
print(f'Part1: {part1}')


seen = set()
groups = set()
for dst in info:
    group = tuple(prog for prog in info if walk([prog], dst))
    groups.add(group)

part2 = len(groups)
print(f'Part2: {part2}')
