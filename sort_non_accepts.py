#!/usr/bin/env python3
import re
import os

myCmd = 'cd submissions/ ; git checkout \*Accepted\* ; cd -'
os.system(myCmd)

fileName = 'files.proj'
lines = [line.rstrip('\n') for line in open(fileName) if 'Accepted' not in line]

problems = {}
for line in lines:
    matches = re.findall(r'submissions\/(\d+)', line)
    if matches:
        num = matches[0]
        problems.setdefault(num, []).append(line)

for k in sorted(problems, key=lambda k: len(problems[k])):
    for accepted in problems[k]:
        print(accepted)
