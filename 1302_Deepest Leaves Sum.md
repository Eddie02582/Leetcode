# Deepest Leaves Sum

## 原題目:
```
Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:
        1
       /  \
      2    3
     / \    \
    4   5    6
   /          \
  7            8   
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.


```

## 思路 dfs
dfs,用depth,ans,計錄最深層的值,當level大於depth,則更新depth,ans値



#### Python
``` python
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:      
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
``` 
使用字典
``` python
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:      
        from collections import defaultdict
        if not root:
            return 0
       
        raw_sum = defaultdict(int)
        depth = 0
        def dfs(node,level):
            nonlocal depth
            if not node:
                return
            depth = max(depth,level)
            raw_sum[level] += node.val
            if node.left:
                dfs(node.left,level + 1)
            if node.right:
                dfs(node.right,level + 1)      
        dfs(root,0)
        
        return raw_sum[depth]
``` 


## 思路 bfs
每層更新當層所有節點的和,最後回傳最後一層的和
``` python
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

``` 

