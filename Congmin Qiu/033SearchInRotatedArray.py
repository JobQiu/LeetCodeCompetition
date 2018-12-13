#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:24:04 2018

@author: xavier.qiu
"""


def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        if nums[mid] < nums[l] and target < nums[l]:
            num_mid = nums[mid]
        elif nums[mid] >= nums[l] and target >= nums[l]:
            num_mid = nums[mid]
        elif target < nums[l]:
            num_mid = -9999
        else:
            num_mid = 9999

        if num_mid == target:
            return mid

        if num_mid > target:
            r = mid
        else:
            l = mid + 1

    return l

    pass


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0



nums = [1,3]
target = 3

print(search(nums, target))