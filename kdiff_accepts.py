#!/usr/bin/env python3
import re
import os

myCmd = 'cd submissions/ ; git checkout \*Accepted\* ; cd -'
os.system(myCmd)

fileName = 'files.proj'
lines = [line.rstrip('\n') for line in open(fileName) if 'Accepted' in line and 'submissions' in line]

accepts = {}
for line in lines:
    num = re.findall(r'submissions\/(\d+)', line)[0]
    accepts.setdefault(num, []).append(line)

for k in sorted(accepts, key=lambda k: len(accepts[k]), reverse=True):
    if len(accepts[k]) > 2:
        continue
    for i, val in enumerate(accepts[k]):
        for j in range(i + 1, len(accepts[k])):
            os.system('kdiff3' + ' ' + accepts[k][i] + ' ' + accepts[k][j])
