#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        try:
            if root.left==None and root.right==None:
                return 0
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            return 1+max(ldepth, rdepth)
        except IndexError:
            pass
        
    
    
    # def getTreeDepth(self, s):
    #     return self.maxDepth(s[0])
    
    
    
sol = Solution([3,9,20,None,None,15,7])
print(sol.maxDepth(0))




# =============================================================================
# class Solution:
#     def __init__(self, tree):
#         self.tree = tree
#         
#     def maxDepth(self, root: int) -> int:
#         try:
#             if self.tree[root*2+1]==None and self.tree[root*2+2]==None:
#                 return 0
#             ldepth = self.maxDepth(root*2+1) if self.maxDepth(root*2+1) else 0
#             rdepth = self.maxDepth(root*2+2) if self.maxDepth(root*2+2)!=None else 0
#             return 1+max(ldepth, rdepth)
#         except IndexError:
#             pass
# =============================================================================
