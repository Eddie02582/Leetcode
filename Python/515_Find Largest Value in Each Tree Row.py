# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        from collections import deque
        if not root:
            return []
        
        
        queue = deque([root])  
        ans = []
        while queue:
            length = len(queue)
            raw_max = float('-inf')
            for i in range(length):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                
                raw_max = max(raw_max,node.val)
            ans.append(raw_max)
        return ans

    def largestValues_dfs(self, root: TreeNode) -> List[int]:
        ans = []
        def dfs(node,level):
            if not node:
                return 
            if level >= len(ans):
                ans.append(node.val)
            else:
                ans[level] = max(ans[level],node.val)
            
            if node.left:
                dfs(node.left,level + 1)
            if node.right:
                dfs(node.right,level + 1)
            
        dfs(root,0)
        return ans