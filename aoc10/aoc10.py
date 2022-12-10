#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:11:36 2022

@author: robertnolet
"""

data = [line.strip().split() for line in open('input.txt')]
ops = {'noop':1, 'addx':2}

x, t = 1, 0
signal = []
crt = [['.']*40 for i in range(6)]
for op in data:
    for i in range(ops[op[0]]):
        t += 1
        if t%40 == 20: signal.append(x*t)
        if i==1: x += int(op[1])
        if t%40 in [x-1,x,x+1]: crt[t//40][t%40] = '#'

# Part 1
print(sum(signal))

# Part 2
print('\n'.join(''.join(line) for line in crt))