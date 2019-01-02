#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 20:37:29 2019

@author: xavier.qiu
"""

with open("test.txt") as f:
    content = f.readlines()
f.close()
from collections import defaultdict
res = defaultdict(int)
for line in content:
    key = line.split(" ")[0]
    res[key] += 1

print(res)

with open('somefile.txt', 'a') as f:
    the_file.write('Hello\n')
f.close
    
    
    #%%