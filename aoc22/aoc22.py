#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 14:47:19 2022

@author: robertnolet
"""

import re
import numpy as np

pat = re.compile(r'(\d+|[LR])')

lines, moves = open('input.txt').read().split('\n\n')

moves = pat.findall(moves.strip())
lines = lines.split('\n')
n = len(lines)//4
m = max(len(line) for line in lines)//3

grids = []
glocs = []
for i in range(4):
    for j in range(4):
        if len(lines[n*i]) > m*j and lines[n*i][m*j] != ' ':
            grid = np.full((n,m), '.')
            for y in range(n):
                grid[y,:] = list(lines[n*i+y][m*j:m*j+m])
            grids.append(grid)
            glocs.append((i,j))

R = ( 1, 0)
L = (-1, 0)
U = ( 0,-1)
D = ( 0, 1)

# Test input conns
# conns1 = [{U:(4,U),L:(0,L),R:(0,R),D:(3,D)},
#           {U:(1,U),L:(3,L),R:(2,R),D:(1,D)},
#           {U:(2,U),L:(1,L),R:(3,R),D:(2,D)},
#           {U:(0,U),L:(2,L),R:(1,R),D:(4,D)},
#           {U:(3,U),L:(5,L),R:(5,R),D:(0,D)},
#           {U:(5,U),L:(4,L),R:(4,R),D:(5,D)}]
                                               
# conns2 = [{U:(1,D),L:(2,D),R:(5,L),D:(3,D)},
#           {U:(0,D),L:(5,U),R:(2,R),D:(4,U)},
#           {U:(0,R),L:(1,L),R:(3,R),D:(4,R)},
#           {U:(0,U),L:(2,L),R:(5,D),D:(4,D)},
#           {U:(3,U),L:(2,U),R:(5,R),D:(1,U)},
#           {U:(3,L),L:(4,L),R:(0,L),D:(1,R)}]

# Real input conns
conns1 = [{U:(4,U),L:(1,L),R:(1,R),D:(2,D)},
          {U:(1,U),L:(0,L),R:(0,R),D:(1,D)},
          {U:(0,U),L:(2,L),R:(2,R),D:(4,D)},
          {U:(5,U),L:(4,L),R:(4,R),D:(5,D)},
          {U:(2,U),L:(3,L),R:(3,R),D:(0,D)},
          {U:(3,U),L:(5,L),R:(5,R),D:(3,D)}]
                                               
conns2 = [{U:(5,R),L:(3,R),R:(1,R),D:(2,D)},
          {U:(5,U),L:(0,L),R:(4,L),D:(2,L)},
          {U:(0,U),L:(3,D),R:(1,U),D:(4,D)},
          {U:(2,R),L:(0,R),R:(4,R),D:(5,D)},
          {U:(2,U),L:(3,L),R:(1,L),D:(5,L)},
          {U:(3,U),L:(0,D),R:(4,U),D:(1,D)}]

for conns in [conns1, conns2]:
    dx, dy = R
    face = 0
    x = np.argmax(grids[face][0] == '.')
    y = 0
    for move in moves:
        if move == 'L':
            dx, dy = dy, -dx
        elif move == 'R':
            dx, dy = -dy, dx
        else:
            for i in range(int(move)):
                grids[face][(y,x)] = 'o'
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    nface, ndx, ndy, nx, ny = face, dx, dy, x+dx, y+dy
                else:
                    nface, (ndx, ndy) = conns[face][(dx,dy)]
                    if (ndx,ndy) == U:
                        ny = n-1
                        if (dx,dy) == U:
                            nx = x 
                        elif (dx,dy) == D:
                            nx = m-1-x
                        elif (dx,dy) == R:
                            nx = y
                        else:
                            nx = n-1-y
                    if (ndx,ndy) == D:
                        ny = 0
                        if (dx,dy) == U:
                            nx = m-1-x
                        elif (dx,dy) == D:
                            nx = x 
                        elif (dx,dy) == R:
                            nx = n-1-y
                        else:
                            nx = y
                    if (ndx,ndy) == R:
                        nx = 0
                        if (dx,dy) == L:
                            ny = n-1-y
                        elif (dx,dy) == R:
                            ny = y
                        elif (dx,dy) == U:
                            ny = x
                        else:
                            ny = m-1-x
                    if (ndx,ndy) == L:
                        nx = m-1
                        if (dx,dy) == L:
                            ny = y
                        elif (dx,dy) == R:
                            ny = n-1-y
                        elif (dx,dy) == U:
                            ny = m-1-x
                        else:
                            ny = x
                if grids[nface][ny,nx] in '.o':
                    face, dx, dy, x, y = nface, ndx, ndy, nx, ny
                else:
                    break
    score = {R:0, D:1, L:2, U:3}
    i,j = glocs[face]
    print(1000*(i*n+y+1) + 4*(j*m+x+1) + score[(dx,dy)])        
                  
                

                
