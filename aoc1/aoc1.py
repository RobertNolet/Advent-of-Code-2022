#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:39:09 2022

@author: robertnolet
"""

file = open('input.txt')
data = [sum(int(line) for line in block.split('\n')) for block in file.read().split('\n\n')]

# Part 1
print(max(data))

# Part 2
print(sum(sorted(data)[-3:]))