#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:22:09 2022

@author: robertnolet
"""

import numpy as np

moves = [(0,1),(-1,1),(1,1),(0,0)]

data = [[[int(x) for x in item.split(',')] for item in line.split('->')] for line in open('input.txt')]

ymax = max(item[1] for line in data for item in line)
xmin = 500-ymax-3
xmax = 500+ymax+3
ymin = 0

start = (500-xmin,0)

cmap = np.full(((xmax-xmin),ymax+3), '.')

for line in data:
    x1, y1 = line[0]
    for x2, y2 in line[1:]:
        cmap[min(x1,x2)-xmin:max(x1,x2)-xmin+1,
             min(y1,y2)-ymin:max(y1,y2)-ymin+1] = '#'
        x1, y1 = x2, y2
cmap[:,ymax+2] = '#'

def onestep(cmap):
    x, y = start
    dy = 1
    while dy != 0:
        dx, dy = next((dx, dy) for dx, dy in moves if cmap[x+dx,y+dy] == '.')
        x,y = x+dx, y+dy
    cmap[x,y] = 'o'
    return x,y
        
# Part 1
y = 0
i = 0
while y<ymax:
    i += 1
    x,y = onestep(cmap)
print(i-1)

# Part 2
while cmap[start] == '.':
    i += 1
    x,y = onestep(cmap)
    
print(i)