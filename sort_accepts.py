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
    for accepted in accepts[k]:
        print(accepted)
