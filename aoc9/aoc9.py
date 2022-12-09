#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:05:43 2022

@author: robertnolet
"""


dirs = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
data = [(line[0], int(line[2:])) for line in open('input.txt')]


def sign(d):
    return d//abs(d) if abs(d)>0 else 0

def move(hx,hy,tx,ty):
    if abs(hx-tx) < 2 and abs(hy-ty) < 2:
        return tx,ty
    return tx+sign(hx-tx), ty+sign(hy-ty)    
    
def simulate(knots, data):
    visited = {knots[-1]}
    for d, n in data:
        dx, dy = dirs[d]
        for i in range(n):
            knots[0] = (knots[0][0]+dx, knots[0][1]+dy)
            for j in range(1, len(knots)):
                knots[j] = move(*knots[j-1], *knots[j])
                visited.add(knots[-1])
    return len(visited)
        
# Part 1
print(simulate([(0,0)]*2,data))

# Part 2
print(simulate([(0,0)]*10,data))
