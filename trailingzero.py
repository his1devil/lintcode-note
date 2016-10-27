#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    返回阶乘中0的个数
    求质因数乘积中5的个数
    """
    def trailingzero(self, n):
        if n < 0:
            return -1
        count = 0
        while n > 0:
            n = n / 5
            count += n
        return count
