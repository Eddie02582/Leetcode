#  Path Sum


## 原題目:
```
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]  1
```

## 思路
同path sum 只是多記錄了結果


## Code



#### Python

```python
class Solution:
    def pathSum(self, root, sum):        
        def dfs(node,total,sol):
            total = total + node.val   
            sol = sol + [node.val]                        
            if node.left:
                dfs(node.left,total,sol) 
            if node.right:
                dfs(node.right,total,sol)      
            if not node.left and not node.right :
                if sum == total:
                    res.append(sol[:])
                return          
        res = []
        if not root:
            return []
        dfs(root,0,[])     
        return res  
```








