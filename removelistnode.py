#! /usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    删除链表中等于给定值val的所有节点
    1->2->3->3->4->5 val=3
    return 1->2->4->5
    """
    def removeElements(self, head, val):
        prev = ListNode(0)
        prev.next = head
        current = prev
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return prev.next
