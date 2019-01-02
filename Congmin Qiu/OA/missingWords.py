#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 20:45:35 2019

@author: xavier.qiu
"""


def missingWords(s, t):
    l1 = s.split(" ")
    l2 = t.split(" ")
    res = []
    i = 0
    for j in range(len(l2)):
        while l1[i] != l2[j]:
            res.append(l1[i])
            i += 1
    i += 1
    while i < len(l1):
        res.append(l1[i])
        i += 1
    return res


s = "this is stupid"
t = "is"

res = missingWords(s, t)
print(res)

# %%
