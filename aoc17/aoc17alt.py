#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 08:58:52 2022

@author: robertnolet
"""

import numpy as np
import matplotlib.pyplot as plt

moves = [1 if c == '>' else -1 for c in list(open('input.txt').readline())]

shapes = {
    0:(['..####.']),
    
    1:(['...#...',
        '..###..',
        '...#...']),
    
    2:(['....#..',
        '....#..',
        '..###..']),
    
    3:(['..#....',
        '..#....',
        '..#....',
        '..#....']),
    
    4:(['..##...',
        '..##...'])}

class Shape:
    def __init__(self, n, h):
        self.shape = {(x,y+h) for x in range(7) for y, line in enumerate(shapes[n%5][::-1]) if line[x] == '#'}

    def canmove(self, grid, dx):
        return not any(x+dx < 0 or x+dx > 6 or (x+dx,y) in grid for x,y in self.shape)
    
    def move(self, dx):
        self.shape = {(x + dx,y) for x,y in self.shape}

    def candrop(self, grid):
        return not any((x, y-1) in grid for x,y in self.shape)
    
    def drop(self):
        self.shape = {(x, y-1) for x,y in self.shape}
        
    def merge(self, grid):
        grid.update(self.shape)


def onestep(grid, s, t):
    dx = moves[t%len(moves)]
    if s.canmove(grid, dx):
        s.move(dx)
    if s.candrop(grid):
        s.drop()
        return False
    s.merge(grid)
    return True

# Part 1
grid = {(x,0) for x in range(7)}
ymax = 0
n = 0
t = 0
s = Shape(n,4)
while n < 2022:
    if onestep(grid, s, t):
        ymax = max(y for x,y in grid)
        n += 1
        s = Shape(n, ymax+4)
    t += 1

print(ymax)    


# Part 2
grid = {(x,0) for x in range(7)}
profiles = []
heights = []
profile = ([0]*7, 0, 0)
ymax = 0
n = 0
t = 0
s = Shape(n,4)
while profile not in profiles:
    if onestep(grid, s, t):
        ymax = max(y for x,y in grid)
        heights.append(ymax)
        n += 1
        s = Shape(n, ymax+4)
        profiles.append(profile)
        profile = [max(y for x1,y in grid if x1==x2) for x2 in range(7)]
        profile = ([y - min(profile) for y in profile], t % len(moves), n % 5)    
    t += 1

i = profiles.index(profile)
d = n - i
dh = heights[n-1] - heights[i-1]

while n%d != 1000000000000%d:
    if onestep(grid, s, t):
        ymax = max(y for x,y in grid)
        n += 1
        s = Shape(n, ymax+4)
    t += 1

bigy = (1000000000000-n)//d*dh
print(bigy + ymax)    