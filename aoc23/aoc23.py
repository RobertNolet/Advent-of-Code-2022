#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:08:35 2022

@author: robertnolet
"""

import numpy as np

elves = {(y,x) for y,line in enumerate(open('input.txt')) for x,c in enumerate(line) if c == '#'}

N  = (-1, 0)
NE = (-1, 1)
E  = ( 0, 1)
SE = ( 1, 1)
S  = ( 1, 0)
SW = ( 1,-1)
W  = ( 0,-1)
NW = (-1,-1)

surr = [N,NE,E,SE,S,SW,W,NW]
moves = [(N, (N, NE, NW)),
         (S, (S, SE, SW)),
         (W, (W, NW, SW)),
         (E, (E, NE, SE))]

def display(elves):
    my = min(y for y,x in elves)
    mx = min(x for y,x in elves)
    wy = max(y for y,x in elves) - min(y for y,x in elves) + 1
    wx = max(x for y,x in elves) - min(x for y,x in elves) + 1
    dis = np.full((wy,wx), '.')
    for y,x in elves:
        dis[y-my,x-mx] = '#'
    for i in range(wy):
        print(''.join(dis[i]))

def propose(y,x, moves):
    if not elves.isdisjoint((y+dy,x+dx) for dy,dx in surr):
        for (my,mx), test in moves:
            if elves.isdisjoint((y+dy,x+dx) for dy,dx in test):
                return y+my,x+mx
    return y,x

def onestep(elves, moves):
    prop = {}
    m = False
    for elf in elves:
        pos = propose(*elf, moves)
        if pos in prop:
            prop[pos].add(elf)
        else:
            prop[pos] = {elf}
    elves = set()
    for pos, locs in prop.items():
        if len(locs) == 1:
            m = m or (pos not in locs)
            elves.add(pos)
        else:
            elves.update(locs)
    return elves, m



# Part 1
m = True
for t in range(1,11):
    elves, m = onestep(elves, moves)
    moves = moves[1:] + [moves[0]]

wy = max(y for y,x in elves) - min(y for y,x in elves) + 1
wx = max(x for y,x in elves) - min(x for y,x in elves) + 1
print(wy*wx - len(elves))

# Part 2
while m:
    elves, m = onestep(elves, moves)
    moves = moves[1:] + [moves[0]]
    t += 1
print(t)
