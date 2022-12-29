#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:13:45 2022

@author: robertnolet
"""

def display(pos):
    print([data[i] for p,i in sorted((p,i) for i,p in pos.items())])

def mix(pos, data):
    n = len(pos)
    for i in range(n):
        p = pos[i]
        np = (pos[i]+data[i])%(n-1)
        if np == 0: np = n-1
        for j in pos:
            if p < pos[j] <= np: 
                pos[j] -= 1
            elif np <= pos[j] < p:
                pos[j] += 1
        pos[i] = np
    return pos

data = [int(s) for s in open('input.txt')]
pos = {i:i for i in range(len(data))}   #{new:old}
pos = mix(pos, data)    
vals = []
for k in [1000,2000,3000]:
    vals.append(next(data[i] for i,p in pos.items() if p == (pos[data.index(0)]+k)%len(pos)))
    
print(sum(vals))

key = 811589153
data = [x*key for x in data]
pos = {i:i for i in range(len(data))}   #{new:old}

for t in range(10):
    pos = mix(pos, data)


vals = []
for k in [1000,2000,3000]:
    vals.append(next(data[i] for i,p in pos.items() if p == (pos[data.index(0)]+k)%len(pos)))

print(sum(vals))