# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])        
        while queue:          
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                if i == 0:
                    ans.append(node.val)
        
        return ans

    def rightSideView_dfs(self, root: TreeNode) -> List[int]:
        ans = []
        def dfs(node,level):
            if not node:
                return 
            if level == len(ans):
                ans.append(node.val)
            if node.right:
                dfs(node.right,level + 1)            
            if node.left:
                dfs(node.left,level + 1)               
        
        dfs(root,0)
        return ans