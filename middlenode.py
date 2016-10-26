#! /usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):
    """
    链表中点
    返回链表中点
    Given 1->2->3 return 2
    Given 1->2 return 1
    """
    def middleNode(self, head):
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
