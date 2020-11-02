# Find Largest Value in Each Tree Row


## 原題目:
```
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:
        1
       /  \
      3    2
     / \    \
    5   3    9

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,null,2]
Output: [1,2]
Example 5:

Input: root = []
Output: []
```

## 思路bfs
依照每層節點歷遍,計錄該層最大値


#### Python
``` python
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
```

## 思路dfs

``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
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
```



