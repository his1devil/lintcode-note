#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    For a given sorted array(上升序列) and a target number,
    find the first index of this number in O(logn) time
    """
    def binarySearch(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start+1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

