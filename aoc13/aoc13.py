#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 08:11:57 2022

@author: robertnolet
"""

def lessthan(left, right):
    for a,b in zip(left, right):
        if type(a) == int and type(b) == int: 
            if a != b: return a<b
        else:
            if type(a) == int: a = [a]
            if type(b) == int: b = [b]
            res = lessthan(a,b)
            if res is not None: return res
    return len(left) < len(right) if len(left) != len(right) else None

data = [b.split('\n') for b in open('input.txt').read().split('\n\n')]
packets = [(eval(a), eval(b)) for a,b in data]

# Part 1
print(sum(i+1 for i, (a,b) in enumerate(packets) if lessthan(a,b)))

# Part 2
i1 = sum(lessthan(a, [[2]]) + lessthan(b, [[2]]) for a,b in packets) + 1
i2 = sum(lessthan(a, [[6]]) + lessthan(b, [[6]]) for a,b in packets) + 2
print(i1*i2)
    