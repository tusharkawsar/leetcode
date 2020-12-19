# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = [0]
        self.depth(root, diameter)
        return diameter[0]
        
    def depth(self, root, diameter):
        if root is None: return 0
        
        leftHeight = self.depth(root.left, diameter)
        rightHeight = self.depth(root.right, diameter)
        diameter[0] = max(diameter[0], leftHeight+rightHeight)
        return 1 + max(leftHeight, rightHeight)
        
        
        
