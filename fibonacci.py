#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    Find the Nth number in Fibonacci sequence
    given 1 return 0
    given 2 return 1
    ...
    """
    def fibonacci(self, n):
        memo = {1:0, 2:1}
        return fib(n, memo)

    def fib(n, memo):
        if not n in memo:
            memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]
