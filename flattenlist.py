#! /usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    """
    Given a list, each element in the list can be a list or integer.
    Flatten it into a simply list with integers.
    递归
    """
    def flatten(self, nestedList):
        result = []
        if isinstance(nestedList, int):
            return [nestedList]
        for i in nestedList:
            result.extend(self.flatten(nestedList))
        return result

