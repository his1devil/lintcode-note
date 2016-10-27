#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Stack(object):
    """
    Implement a stack. You can use any data structure inside a stack except stack itself to implement it.
    """
    def __init__(self):
        self.items = []

    def push(self,x):
        self.items.append(x)

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

