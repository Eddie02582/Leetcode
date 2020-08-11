# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        paths = []
        def dfs(node,n):
            n = n * 10 + node.val
            if not node.right and not node.left:
                paths.append(n)
                return
            if node.left:
                dfs(node.left,n)
            if node.right:
                dfs(node.right,n)            
        
        if not root:
            return 0
        dfs(root,0)
        return sum(paths)