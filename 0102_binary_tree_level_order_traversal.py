# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        level = [root]
        ans = []
        
        while level:
            ans.append([item.val for item in level])
            
            temp = []
            for item in level:
                temp.append(item.left)
                temp.append(item.right)
            level = [item for item in temp if item]
            
        return ans
