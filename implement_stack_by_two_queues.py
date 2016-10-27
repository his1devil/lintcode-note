#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Stack(object):
    """
    双队列实现栈
    意味着不能直接pop队列中的最后一个元素
    实现方法是用一个中转or tmp queue，看似是一个queue，少了中转次数
    """
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        """
        return nothing, pop the top of the stack
        """
        for _ in xrange(len(self.queue)-1):
            self.queue.append(self.queue.pop(0))
        self.queue.pop(0)

    def top(self):
        """
         return the top of the stack
        """
        top = None
        for _ in xrange(len(self.queue)):
            top = self.queue.pop(0)
            self.queue.append(top)
        return top
