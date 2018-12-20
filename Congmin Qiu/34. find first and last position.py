#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:21:13 2018

@author: xavier.qiu
"""

nums = [5,7,7,8,8,10]
target = 8


#%%

def searchInsert(nums, target ): 
    left = 0 
    right= len(nums)
    
    while left < right:
        mid = (left + right ) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid+1
    return left 

res = searchInsert(nums, 7.5)

res2 = searchInsert(nums, 8.5)