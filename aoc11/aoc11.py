#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 10:27:26 2022

@author: robertnolet
"""

import re
from math import prod

pat = re.compile(r'  Operation: new = (old|\d+) ([\*\+]) (old|\d+)')

ops = {'+': lambda x,y: (x+y),
       '*': lambda x,y: (x*y)}

class Monkey:
    def __init__(self, lines):
        self.items = [int(s) for s in re.findall(r'(\d+)', lines[1])]
        self.x, self.op, self.y = pat.match(lines[2]).groups()
        self.tvalue = int(re.findall(r'(\d+)', lines[3])[0])
        p = [int(re.findall(r'(\d+)', lines[i])[0]) for i in [4,5]]
        self.partners = {True: p[0], False: p[1]}
        self.activity = 0
        
    def catch(self, item):
        self.items.append(item)
        
    def inspect(self, item):
        self.activity += 1
        x = item if self.x == 'old' else int(self.x)
        y = item if self.y == 'old' else int(self.y)
        return ops[self.op](x, y)
    
    def test(self, item):
        return (item % self.tvalue) == 0
    
    def turn(self, part, mod):
        div = 3 if part == 1 else 1
        items = [self.inspect(item)//div % mod for item in self.items]
        self.items = []
        return [(item, self.partners[self.test(item)]) for item in items]


rawdata = open('input.txt').read().split('\n\n')

# Part 1
monkeys = [Monkey(m.split('\n')) for m in rawdata]
mod = prod(m.tvalue for m in monkeys)

for i in range(20):
    for m in monkeys:
        for item, dest in m.turn(1, mod):
            monkeys[dest].catch(item)

a, b = sorted(m.activity for m in monkeys)[-2:]
print(a*b)

# Part 2
monkeys = [Monkey(m.split('\n')) for m in rawdata]

for i in range(10000):
    for m in monkeys:
        for item, dest in m.turn(2, mod):
            monkeys[dest].catch(item)

a, b = sorted(m.activity for m in monkeys)[-2:]
print(a*b)