#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    Given a string and an offset, rotate string by offset. (rotate from left to right)
    offset=2 => "fgabcde"
    """
    def rotateString(self, s, offset):
        # 防止offset越界，offset 对len(s)取模
        if s is None or len(s) == 0:
            return -1
        offset = offset % len(s)
        first = s[:len(s) - offset]
        end = s[len(s) - offset:]
        s = first[::-1] + end[::-1]
        s = s[::-1]
        return s

    # 借助mutable structure 原地变换字符串 因为字符串不可变
    def rotateString2(self, s, offset):
        if s is None or len(s) == 0:
            return -1
        offset = offset % len(s)
        self.reverse(s, 0, len(s) - offset - 1)
        self.reverse(s, len(s) - offset, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)

    def reverse(self, _str, start, end):
        while start < end:
            _str[start], _str[end] = _str[end], _str[start]
            start += 1
            end -= 1


