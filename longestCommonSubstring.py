#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def longestCommonSubstring(self, A, B):
        length = 0
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                l = 0
                while i + l < len(A) and j + l < len(B) and A[i+l] == B[j+l]:
                    l += 1
                if l > length:
                    length = l
        return length
