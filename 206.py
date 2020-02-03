#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newlist = None
        newlist_head = newlist
        runner = head
        while runner != None:
            nextnode = runner.next
            runner.next = newlist
            newlist = runner
            runner = nextnode
        return newlist
    
    
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
# printListNode(lsthead)
head = sol.reverseList(lsthead)
printListNode(head)
