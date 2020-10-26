# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        
        level_sum = 0
        queue = deque([root])
        
        while queue:
            level_sum = 0
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)                
                level_sum += node.val           
            
        return level_sum

    def deepestLeavesSum_dfs(self, root: TreeNode) -> int:      
        if not root:
            return 0      
       
        depth = 0
        ans = 0
        def dfs(node,level):
            nonlocal depth,ans
            if not node:
                return
            if level > depth:
                depth = level
                ans = node.val
            elif level == depth:
                ans += node.val    
            if node.left:
                dfs(node.left,level + 1)
            if node.right:
                dfs(node.right,level + 1)      
        dfs(root,0)
        
        return ans