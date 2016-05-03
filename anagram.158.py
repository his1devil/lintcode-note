#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
两个字符串是变位词
写出一个函数 anagram(s, t) 去判断两个字符串是否是颠倒字母顺序构成的
"""

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true of false
    """
    def anagram(self, s, t):
        self.s = s
        self.t = t
        ds = self.check(self.s)
        dt = self.check(self.t)
        if ds == dt:
            return True
        else:
            return False

    def check(self, s):
        self.s = s
        d = {}
        for item in self.s:
            try:
                d[item] += 1
            except KeyError:
                d[item] = 1
        return d
