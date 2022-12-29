#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 17:46:49 2022

@author: robertnolet
"""

import numpy as np
from itertools import combinations

dirs = np.concatenate([np.eye(3, dtype=int), -np.eye(3,dtype=int)])
data = np.array([[int(s)+1 for s in line.split(',')] for line in open('input.txt')])
map3d = np.zeros((25,25,25), dtype=int)
map3d[data[:,0],data[:,1],data[:,2]] = 1

area = ((abs(map3d[1:,:,:] - map3d[:-1,:,:]) == 1).sum() +
        (abs(map3d[:,1:,:] - map3d[:,:-1,:]) == 1).sum() +
        (abs(map3d[:,:,1:] - map3d[:,:,:-1]) == 1).sum())
print(area)

tocheck = {(0,0,0)}
while tocheck:
    nextcheck = set()
    for x,y,z in tocheck:
        map3d[x,y,z] = 1
        for dx, dy, dz in dirs:
            if map3d[x+dx,y+dy,z+dz] == 0:
                nextcheck.add((x+dx,dy+y,z+dz))
        tocheck = nextcheck
        
intarea = ((abs(map3d[1:,:,:] - map3d[:-1,:,:]) == 1).sum() +
           (abs(map3d[:,1:,:] - map3d[:,:-1,:]) == 1).sum() +
           (abs(map3d[:,:,1:] - map3d[:,:,:-1]) == 1).sum())
print(area - intarea)
