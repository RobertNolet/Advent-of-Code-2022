#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:07:00 2022

@author: robertnolet
"""

scores1 = {'A X':4, 'A Y':8, 'A Z': 3,
           'B X':1, 'B Y':5, 'B Z': 9,
           'C X':7, 'C Y':2, 'C Z': 6}

scores2 = {'A X':3, 'A Y':4, 'A Z': 8,
           'B X':1, 'B Y':5, 'B Z': 9,
           'C X':2, 'C Y':6, 'C Z': 7}

data = [line.strip() for line in open('input.txt')]

# Part 1
print(sum(scores1[line] for line in data))

# Part 2
print(sum(scores2[line] for line in data))