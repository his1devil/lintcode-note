#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    """
    对于一个给定的source字符串和一个target字符串，在source字符串中
    找出target字符串出现的第一个位置（从0开始)，如果不存在，返回-1
    """

    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        else:
            for i in xrange(len(source)-len(target)+1):
                for j in xrange(len(target)):
                    if source[i+j] != target[j]:
                        break
                else:
                    return i
            return -1
