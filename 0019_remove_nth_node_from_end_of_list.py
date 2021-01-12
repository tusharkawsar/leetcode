#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# [1,2,3,4,5] 
# 2
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        curr = head
        nxt = head.next
        for i in range(n-1):
            nxt = nxt.next
        
        while nxt != None and nxt.next != None:
            curr = curr.next
            nxt = nxt.next
        # print(curr.val, nxt.val, nxt.next)
        if curr == head and nxt == None:
            return head.next
            
        first = curr
        second = first.next
        third = second.next
        first.next = third
        return head
        
  
def printListNode(head: ListNode):
    while head != None:
        print(head.val)
        head = head.next

lst = ListNode(1)
lsthead = lst
for i in range(1):
    lst.next = ListNode(i+2)
    lst = lst.next
# printListNode(lsthead)
# print(lsthead.next.next.next.next.val)
sol = Solution()
printListNode(sol.removeNthFromEnd(lsthead, 1))