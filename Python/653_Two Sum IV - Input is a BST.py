# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    def findTarget(self, root: Optional[TreeNode], k: int,lookup = {}) -> bool:
        from collections import deque
        number = set()
        queue = deque([root.val])
        
        while queue:
            node = queue.popleft()            
            if k - node.val in number:
                return True
            if node.right:
                queue.append(node.right.val)
            if node.left:
                queue.append(node.left.val)              
            number.add(node.val)
        return False

    def findTarget_dfs(self, root: Optional[TreeNode], k: int) -> bool:
        
        def dfs(root, seen):
            if root == None: return False
            complement = k - root.val
            if complement in seen: return True
            seen.add(root.val)
            return dfs(root.left, seen) or dfs(root.right, seen)
        
        return dfs(root, set())