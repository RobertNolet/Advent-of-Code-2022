#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:01:12 2022

@author: robertnolet
"""

vel = {'>':(0,1), '<':(0,-1), 'v':(1,0), '^':(-1,0)}
dirs = [(0,1),(0,-1),(1,0),(-1,0),(0,0)]

blizz = {(y,x,*vel[d]) for y, line in enumerate(open('input.txt')) for x, d in enumerate(line) if d in '><v^'}
ymax = max(b[0] for b in blizz)
xmax = max(b[1] for b in blizz)
start = (0,1)
end = (ymax+1, xmax)

def validpos(y,x):
    return (0 < y <= ymax and 0 < x <= xmax) or (y,x) in {start,end}

def validmoves(y,x,blizz):
    pos = {(y+dy,x+dx) for dy,dx in dirs if validpos(y+dy,x+dx)}
    return pos.difference((y,x) for y,x,dy,dx in blizz)

def updateblizz(blizz):
    return {((y+dy-1)%ymax+1,(x+dx-1)%xmax+1,dy,dx) for y,x,dy,dx in blizz}

# Part 1
pos = {start}
t = 0
while end not in pos:
    t += 1
    blizz = updateblizz(blizz)
    pos = set.union(*(validmoves(*p, blizz) for p in pos))
print(t)

# Part 2
pos = {end}
while start not in pos:
    t += 1
    blizz = updateblizz(blizz)
    pos = set.union(*(validmoves(*p, blizz) for p in pos))
pos = {start}
while end not in pos:
    t += 1
    blizz = updateblizz(blizz)
    pos = set.union(*(validmoves(*p, blizz) for p in pos))
print(t)
    