# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode,max_value = float('-inf')) -> int:
        if not root:
            return 0            
        count = 1 if root.val >= max_value  else 0 
        max_value = max(max_value,root.val)
        return self.goodNodes(root.left,max_value) + self.goodNodes(root.right,max_value) + count
        
    
    def goodNodes_bfs(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return 0
        queue = deque([(root,root.val)])     
        good = 1
        while queue:
            n = len(queue)
            for i in range(n): 
                node,val = queue.popleft()    
                if node.left:                                        
                    queue.append((node.left,max(val,node.left.val)))
                    if node.left.val >= val:
                        good += 1
                if node.right:
                    queue.append((node.right,max(val,node.right.val)))
                    if node.right.val >= val:
                        good += 1
        
        return good
