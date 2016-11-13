#! /usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):
    """
    翻转一个链表
    1->2_.3->null => 3->2->1->null
    """
    def reverse(self, head):
        cur = None
        while head != None:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
        return cur
