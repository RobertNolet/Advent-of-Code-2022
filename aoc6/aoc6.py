#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 07:05:05 2022

@author: robertnolet
"""

data = open('input.txt').readline()

#  Part 1
print(next(i for i in range(len(data)-4) if len(set(data[i:i+4])) == 4)+4)

# Part 2
print(next(i for i in range(len(data)-14) if len(set(data[i:i+14])) == 14)+14)