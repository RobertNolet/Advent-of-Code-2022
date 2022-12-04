#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:27:31 2022

@author: robertnolet
"""

import re

def contain(a, b, c, d):
    return (a <= c <= d <= b or
            c <= a <= b <= d)

def overlap(a, b, c, d):
    return (a <= c <= b <= d or
            c <= a <= d <= b or
            contain(a, b, c, d))

    
pat = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

data = [list(map(int, pat.match(line).groups())) for line in open('input.txt')]

# Part 1
print(sum(contain(*line) for line in data))

# Part 2
print(sum(overlap(*line) for line in data))