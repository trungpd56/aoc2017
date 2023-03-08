import requests
import os

day = 7
cookies = {"session": "53616c7465645f5fdfb5bea667eec09862e4a70f222dbb5f14618320eec9a629e21a9763642e8104a9e413cd5a0825f9e58a31cd4d0e4f685c8f03c9c800162c"}

r = requests.get(
    f'https://adventofcode.com/2017/day/{day}/input', cookies=cookies)

if not os.path.exists(f"day{day:02}"):
    os.mkdir(f"day{day:02}")
os.chdir(f"day{day:02}")

with open('input.txt', 'w') as f:
    f.write(r.text)

sample = f"""\
#!/usr/bin/env python3

with open('input.txt', 'r') as f:
    lines = f.readlines()


part1 = ""
print(f'Part1: {'{'}part1{'}'}')

part2 = ""
print(f'Part2: {chr(123)}part2{chr(125)}')
"""

if not os.path.isfile(f'day{day:02}.py'):
    with open(f'day{day:02}.py', 'w', newline='\n') as f:
        f.write(sample)
