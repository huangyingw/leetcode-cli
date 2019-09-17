#!/usr/bin/env python3
import re

fileName = 'files.proj'
lines = [line.rstrip('\n') for line in open(fileName) if 'Accepted' in line]

problem_accepts = {}
for line in lines:
    num = re.findall(r'submissions\/(\d+)', line)[0]
    problem_accepts.setdefault(num, []).append(line)

for k in sorted(problem_accepts, key=lambda k: len(problem_accepts[k]), reverse=True):
    for accepted in problem_accepts[k]:
        print(accepted)
