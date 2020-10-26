# Binary Tree Right Side View


## 原題目:
```
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

## 思路 bfs
bfs,計錄每一層最後一個値(右邊的值)


#### Python

```
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        from collections import deque
        if not root:
            return []
        ans = []
        queue = deque([root])        
        while queue:          
            length = len(queue)
            right_value = None
            for i in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                right_value = node.val
            if right_value != None:
                ans.append(right_value)
        return ans
```


## 思路 dfs
dfs,從右邊現歷遍,計錄每層第一次出現得値

``` python
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
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

```

