class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        from collections import deque
        if not root:return []
        queue = deque([root])      
        ans = []
        while queue:
            length = len(queue)
            value  = 0
            for _ in range(length):
                node = queue.popleft()                
                value += node.val
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            
            ans.append(value/length)
        return ans
        