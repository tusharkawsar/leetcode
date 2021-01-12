# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # Merkle Hashing
        
        from hashlib import sha256
        
        def hash_(x):
            S = sha256()
            S.update(x.encode('utf-8'))
            return S.hexdigest()
        
        def merkle(node):
            if not node:
                return '#'
            merkle_left = merkle(node.left)
            merkle_right = merkle(node.right)
            node.merkle = hash_(merkle_left + str(node.val) + merkle_right)
            return node.merkle
        
        def dfs(node):
            if not node:
                return False
            return (node.merkle == t.merkle or dfs(node.left) or dfs(node.right))
            
        merkle(s)
        merkle(t)
        return dfs(s)
        
