#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:41:48 2022

@author: robertnolet
"""

import re

def solver(block1, block2, part):
    # Parse crates
    crates = {int(c):[] for c in block1[-1][1::4]}
    for line in reversed(block1[:-1]):
        for i, c in enumerate(line[1::4]):
            if c != ' ':
                crates[i+1].append(c)
    
    # Parse moves and move crates
    pat = re.compile('move (\d+) from (\d+) to (\d+)')
    for line in block2:
        n, i, j = map(int, pat.match(line).groups())
        if part == 1:
            for k in range(n):
                c = crates[i].pop()
                crates[j].append(c)
        if part == 2:
            crates[j].extend(crates[i][-n:])
            for k in range(n):
                crates[i].pop()
    return ''.join(c[-1] for c in crates.values())

# Read file
block1, block2 = [x.split('\n') for x in open('input.txt').read().split('\n\n')]

# Part 1
print(solver(block1, block2, 1))

# Part 2
print(solver(block1, block2, 2))
