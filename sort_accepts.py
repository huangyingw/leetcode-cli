#!/usr/bin/env python3
import re

fileName = 'files.proj'
lines = [line.rstrip('\n') for line in open(fileName) if 'Accepted' in line]
print('\n'.join(map(str, lines)))

problem_accepts = {}
for line in lines:
    num = re.findall(r'submissions\/(\d+)', line)[0]
    problem_accepts.setdefault(num, []).append(line)

print(problem_accepts)
problem_accepts = sorted(problem_accepts, key=lambda k: len(problem_accepts[k]), reverse=True)
print(problem_accepts)
