#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    Find the last position of a target number in a sorted array
    """
    def lastPosition(self, A, target):
        if A is None or len(A) == 0:
            return -1
        start, end = 0, len(A) - 1
        while start+1 < end:
            mid = start + (end-start) / 2
            if A[mid] == target:
                start = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
