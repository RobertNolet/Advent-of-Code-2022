#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:48:02 2022

@author: robertnolet
"""

dirs = [[0,1],[0,-1],[1,0],[-1,0]]

data = [list(line.strip()) for line in open('input.txt')]
n = len(data)
m = len(data[0])

for y in range(n):
    for x in range(m):
        if data[y][x] == 'S': start = (y,x)
        if data[y][x] == 'E': end = (y,x)
        
def height(c):
    if c == 'S': return ord('a') - 1
    if c == 'E': return ord('z') + 1
    return ord(c)

def connections(y, x, part):
    result = set()
    for dy,dx in dirs:
        if (0 <= y + dy < n and 0 <= x + dx < m and 
            ((part == 1 and height(data[y+dy][x+dx]) <= height(data[y][x]) + 1) or
             (part == 2 and height(data[y+dy][x+dx]) >= height(data[y][x]) - 1))):
            result.add((y+dy,x+dx))
    return result



# Part 1
def solver(part):
    graph = {(y,x): connections(y,x,part) for y in range(n) for x in range(m)}
    t=0
    if part == 1:
        visited = {start}
        tocheck = graph[start]
    elif part == 2:
        visited = {end}
        tocheck = graph[end]
    while True:
        t += 1
        connects = set()
        for y,x in tocheck:
            if (part == 1 and (y,x) == end) or (part == 2 and data[y][x] == 'a'):
                return t
            visited.add((y,x))
            connects.update(graph[y,x])
        tocheck = connects - visited
        
# Part 1
print(solver(1))

# Part 2
print(solver(2))

