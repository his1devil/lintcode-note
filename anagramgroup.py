#! /usr/bin/env python
# -*- coding: utf-8 -*-


import collections
"""
乱序字符串
给出一个字符串数组S，找到其中所有的乱序字符串
如果一个字符串是乱序字符串，那么存在一个字母集合相同
但顺序不同的字符串也在S中
"""

class Solution(object):
    def anagrams(self, strs):
        result = []
        strDict = collections.defaultdict(int)
        for str in strs:
            strDict["".join(sorted(str))] + 1
        for str in strs:
            if strDict["".join(sorted(str))] > 1:
                result.append(str)
        return result

