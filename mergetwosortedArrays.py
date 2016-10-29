#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    Merge two given sorted integer array A and B into a new sorted integer
    """
    def mergeSortedArray(self, A, B):
        if A is None or len(A) == 0:
            return B
        if B is None or len(B) == 0:
            return A
        result = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1

        while i < len(A):
            result.append(A)
            i += 1
        while j < len(B):
            result.append(B)
            j += 1
        return result
