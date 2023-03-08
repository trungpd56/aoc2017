#!/usr/bin/env python3
from collections import defaultdict


def walk(visited):
    if len(info[visited]) == 0:
        return None
    trees = defaultdict(dict)
    for i in info[visited]:
        trees[visited][i] = (walk(i))
    return trees


with open('input.txt', 'r') as f:
    lines = f.readlines()

info = defaultdict(list)
for line in lines:
    line = line.strip()
    toks = line.split()
    if '->' in line:
        part = line.strip().split(' -> ')
        info[toks[0]].extend(part[1].split(', '))
    else:
        info[toks[0]] = []


part1 = ""
print(f'Part1: {part1}')

part2 = ""
print(f'Part2: {part2}')
