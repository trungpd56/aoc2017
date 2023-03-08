#!/usr/bin/env python3
from collections import deque
from functools import reduce
import operator


def hq(ins, t=1):
    queue = list(range(256))
    skip = 0
    pos = 0
    for _ in range(t):
        for n in ins:
            queue = queue[:n][::-1] + queue[n:]
            queue = deque(queue)
            for i in range((n + skip) % len(queue)):
                queue.append(queue.popleft())
            pos += ((n + skip) % len(queue))
            skip += 1
            queue = list(queue)
    queue = deque(enumerate(queue))
    while True:
        if queue[pos % len(queue)][0] == 0:
            break
        queue.append(queue.popleft())
    return [n[1] for n in queue]


with open('input.txt', 'r') as f:
    data = f.read().strip()

ins = list(map(int, data.split(',')))
queue = hq(ins)
part1 = queue[0] * queue[1]
print(f'Part1: {part1}')

ins2 = [ord(c) for c in data] + [17, 31, 73, 47, 23]
queue2 = hq(ins2, t=64)
dense = []
for n in range(0, len(queue2), 16):
    result = reduce(operator.xor, [n for n in queue2[n:n+16]])
    dense.append(result)
part2 = ''.join([f'{x:02X}' for x in dense]).lower()
print(f'Part2: {part2}')
