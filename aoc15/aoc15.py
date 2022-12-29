#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 09:04:03 2022

@author: robertnolet
"""

import re
from itertools import combinations

pat = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')

def manhattan(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

class Sensor:
    def __init__(self, s):
        self.x, self.y, self.bx, self.by = map(int, pat.match(s).groups())
        self.r = manhattan(self.x, self.y, self.bx, self.by)
    
    def __str__(self):
        return f"Sensor: {self.x, self.y}, Beacon {self.bx, self.by}, Radius {self.r}"
    
    def x_at_y(self, y):
        dx = self.r - abs(self.y-y)
        if dx < 0:
            return self.x, self.x
        if y == self.by and self.x - dx == self.bx:
            return self.x - dx + 1, self.x + dx + 1
        if y == self.by and self.x + dx == self.bx:
            return self.x - dx, self.x + dx
        return self.x - dx, self.x + dx + 1
    
    def width_at_y(self, y):
        x1, x2 = self.x_at_y(y)
        return x2-x1
    
    def dist_to(self, other):
        return manhattan(self.x, self.y, other.x, other.y)
    
    def overlaps(self, other):
        return self.dist_to(other) < self.r + other.r
    
    def overlap_at_y(self, other, y):
        x1,x2 = self.x_at_y(y)
        x3,x4 = other.x_at_y(y)
        xmin = min(x1, x3)
        xmax = max(x2, x4)
        res = max(0, self.width_at_y(y) + other.width_at_y(y) - (xmax - xmin))
        return res


data = [Sensor(line) for line in open('input.txt')]

y = 10
y = 2000000

# Part 1
ints = []
for s in data:
    a, b = s.x_at_y(y)
    for x1, x2 in ints:
        if a <= x1 < x2 <= b:
            ints.remove((x1,x2))
        else:
            if x1 <= a < x2:
                a = x2
            if x1 <= b < x2:
                b = x1
            if b <= a:
                break
    if b > a:
        ints.append((a,b))
print(sum(x2-x1 for x1, x2 in ints))

# Part 2
def part2(data):
    beacons = [(s.bx, s.by) for s in data]
    for y in range(4000001):
        ints = []
        for s in data:
            a, b = s.x_at_y(y)
            a = max(0,a)
            b = min(b,4000001)
            for x1, x2 in ints.copy():
                if a <= x1 < x2 <= b:
                    ints.remove((x1,x2))
                else:
                    if x1 <= a < x2:
                        a = x2
                    if x1 <= b < x2:
                        b = x1
                    if b <= a:
                        break
            if b > a:
                ints.append((a,b))
        ints.sort()
        for (x1,x2),(x3,x4) in zip(ints[:-1], ints[1:]):
            if x2 != x3 and (x2,y) not in beacons:
                return x2, y
            
x, y = part2(data)
print(x*4000000+y)
