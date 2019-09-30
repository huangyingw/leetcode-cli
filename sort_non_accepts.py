#!/usr/bin/env python3
import re
import os

myCmd = 'cd submissions/ ; git checkout \*Accepted\* ; cd -'
os.system(myCmd)

fileName = 'files.proj'
lines = [line.rstrip('\n') for line in open(fileName) if 'Accepted' not in line]

non_accepts = {}
for line in lines:
    matches = re.findall(r'submissions\/(\d+)', line)
    if matches:
        num = matches[0]
        non_accepts.setdefault(num, []).append(line)

for k in sorted(non_accepts, key=lambda k: len(non_accepts[k])):
    for non_accept in non_accepts[k]:
        print(non_accept)
