#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    
def printListNode(head: ListNode):
    dummyhead = head
    while dummyhead != None:
        print(dummyhead.val)
        dummyhead = dummyhead.next
    
sol = Solution()
lst = ListNode(1)
lsthead = lst
for i in range(5):
    lst.next = ListNode(i+2)
    lst = lst.next
printListNode(lsthead)
sol.deleteNode([4,5,1,9], 5)

        

