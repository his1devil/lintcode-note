#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    升序排列一组整数，使用O(n²)算法
    """
    def sortIntegers(self, A):
        swap = True
        passnumber = len(A) - 1
        while passnumber > 0 and swap:
            # 记录是否swapped
            swap = False
            for i in range(passnumber):
                if A[i] > A[i+1]:
                    swap = True
                    A[i], A[i+1] = A[i+1], A[i]
            passnumber -= 1
        return A

