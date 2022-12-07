#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:12:20 2022

@author: robertnolet
"""


class Directory:
    def __init__(self, output):
        self.subdirs = {}
        self.size = 0
        for item in output:
            if item == '$ cd ..':
                return
            elif item == '$ cd \\':
                pass
            elif item[:4] == '$ cd':
                self.subdirs[item[5:]] = Directory(output)
                self.size += self.subdirs[item[5:]].size
            elif item[:3] == 'dir':
                pass
            elif item[0] != '$':
                self.size += int(item.split()[0])

    def sumsizebelow(self, n):
        result = 0 if self.size > n else self.size
        return result + sum(d.sumsizebelow(n) for d in self.subdirs.values())
        
    def sizes(self):
        result = [self.size] 
        for d in self.subdirs.values():
            result.extend(d.sizes())
        return result
    
maindir = Directory(line.strip() for line in open('input.txt'))

# Part 1
print(maindir.sumsizebelow(100000))

# Part 2
print(min(x for x in maindir.sizes() if x > maindir.size - 40000000))