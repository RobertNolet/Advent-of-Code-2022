#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:18:39 2022

@author: robertnolet
"""

def prio(c):
    if type(c) == set: c = c.pop()
    return  ord(c) - ord('A') + 27 if c.isupper() else ord(c) - ord('a') + 1

def half(x):
    return [(r[:len(r)//2], r[len(r)//2:]) for r in x]
    
def triple(x):
    return [(x[i], x[i+1], x[i+2]) for i in range(0, len(x), 3)]
            
data = [r.strip() for r in open('input.txt')]

# Part 1
print(sum(prio(set(a) & set(b)) for a,b in half(data)))

# Part 2
print(sum(prio(set(a) & set(b) & set(c)) for a,b,c in triple(data)))