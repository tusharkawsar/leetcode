# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t = TreeNode()
        if t1 is not None and t2 is not None:
            t.val = t1.val + t2.val
            t.left = self.mergeTrees(t1.left, t2. left)
            t.right = self.mergeTrees(t1.right, t2. right)
        elif t1 is None:
            t = t2
        elif t2 is None:
            t = t1
        return t
        
        
        
        
