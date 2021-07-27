#  Path Sum


## 原題目:
```
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```

## 思路1 



## Code



#### Python

```python
class Solution(object):
    def hasPathSum(self, root: sum):        
        def dfs(node,total):
            total = total + node.val                           
            if node.left and dfs(node.left,total):               
                return True
            if node.right and dfs(node.right,total ):                
                return True
            if not node.left and not node.right and sum == total:
                return True

            return False
        
        if not root:
            return False

        return dfs(root,0)   
```

```python
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:

        def dfs(root,res):            
            if not root:                
                if res == 0:                  
                    return True
                return False
            
            res -= root.val            
            if dfs(root.left,res):
                return True
            if dfs(root.right,res):
                return True
        
        return dfs(root,targetSum)
```






