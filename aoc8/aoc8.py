#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:25:52 2022

@author: robertnolet
"""

import numpy as np

data = np.array([[int(c) for c in line.strip()] for line in open('input.txt')])
n,m = data.shape

def valid(i,j):
    return 0 <= i < n and 0 <= j < m

vis = 0
maxres = 0
for i in range(n):
    for j in range(m):
        res = 1
        edges = 0
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            k=1
            while valid(i+k*di,j+k*dj) and data[i+k*di,j+k*dj] < data[i,j]:
                k += 1
            if valid(i+k*di, j+k*dj):
                k += 1
            else:
                edges += 1
            res *= (k-1)
        vis += (edges > 0)
        maxres = max(maxres, res)

# Part 1
print(vis)

# Part 2            
print(maxres)