#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

# Definition for singly-linked list.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.curr_list = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:    
       
        if root is not None:
            # print(self.curr_list)
            if root.left is None and root.right is None: # this will actually be covered by the condition for middle node, so not needed
                self.curr_list.append(root.val)
                return self.curr_list
            if root is not None and root.left is not None:
                self.inorderTraversal(root.left)
                print("root.left traversed",self.curr_list)
            self.curr_list.append(root.val)
            print("root traversed",self.curr_list)
            if root.right is not None:
                self.inorderTraversal(root.right)
                print("root.right traversed",self.curr_list)
            return self.curr_list
    
    
def printListNode(head: TreeNode):
    dummyhead = head
    while dummyhead != None:
        print(dummyhead.val)
        dummyhead = dummyhead.next    
    
sol = Solution()
lst = TreeNode(1)
lsthead = lst
for i in range(5):
    lst.left = TreeNode(i+1)
    lst.right = TreeNode(i+2)
#     lst = lst.next
# printListNode(lsthead)
# head = sol.reverseList(lsthead)
# printListNode(head)


