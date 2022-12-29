#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 13:47:20 2022

@author: robertnolet
"""

from itertools import count

def parse(line, isroot = False):
    if line.isnumeric():
        return lambda data: int(line)
    elif isroot:
        return lambda data: data[line[:4]](data) - data[line[-4:]](data)
    elif line[5] == '+':
        return lambda data: data[line[:4]](data) + data[line[-4:]](data)
    elif line[5] == '-':
        return lambda data: data[line[:4]](data) - data[line[-4:]](data)
    elif line[5] == '*':
        return lambda data: data[line[:4]](data) * data[line[-4:]](data)
    elif line[5] == '/':
        return lambda data: data[line[:4]](data) // data[line[-4:]](data)


# Part 1
data = {line[:4]: parse(line.strip()[6:]) for line in open('input.txt')}

print(data['root'](data))

# Part 2
data = {line[:4]: parse(line.strip()[6:], line[:4] == 'root') for line in open('input.txt')}

def f(i):
    data['humn'] = lambda x: i
    return data['root'](data)

x1 = 0
x2 = 1000
y1 = f(x1)
y2 = f(x2)
while y1*y2 > 0:
    dydx = (y2-y1)//1000
    x1 = x1 - y1//dydx
    y1 = f(x1)
    if y1 < 0:
        x2 = x1 - 1000
    else:
        x2 = x1 + 1000
    y2 = f(x2)
for x in range(x1,x2):
    if f(x) == 0:
        print(x)
        break
    