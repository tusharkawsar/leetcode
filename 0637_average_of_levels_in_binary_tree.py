# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level = [root]
        avg_level = []
        
        while len(level) > 0:
            sum = 0
            for item in level:
                sum += item.val
            avg_level.append(sum/len(level))
            dup_level = level
            level = []
            
            for item in dup_level:
                curr = item
                if curr.left is not None: level.append(curr.left) 
                if curr.right is not None: level.append(curr.right)
            
        return(avg_level)

