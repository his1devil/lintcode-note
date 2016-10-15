#! /usr/bin/env python
# -*- coding: utf-8 -*-

import collections


class Solution(object):
    """
    比较两个字符串A和B，确定A中是否包含B中所有字符
    字符串A和B中字符都是大写字母
    """
    def compareStrings(self, A, B):
        str = collections.defaultdict(int)
        for i in A:
            str[i] += 1
        for j in B:
            str[j] -= 1
            if j not in str or str[j] < 0:
                return False
        return True
