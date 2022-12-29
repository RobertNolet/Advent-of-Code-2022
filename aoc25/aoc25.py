#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:40:20 2022

@author: robertnolet
"""

from math import log

conv = {'2':2,'1':1,'0':0,'-':-1,'=':-2}
dcnv = ['=','-','0','1','2']

n = sum(conv[c]*(5**i) for line in open('input.txt') for i,c in enumerate(line.strip()[::-1]))
n += sum(2*(5**i) for i in range(int(log(n,5))+1))

res = ''
while n > 0:
    res = dcnv[n%5] + res
    n = n//5

print(res)