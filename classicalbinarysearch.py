#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    Find any position of a target number in a sorted array.
    Return -1 if target does not exist.
    """
    def findPosition(self, A, target):
        # 相邻就退出
        if len(A) == 0 or A is None:
            return -1
        start, end = 0, len(A) - 1
        while start+1 < end:
            mid = start + (end-start) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
