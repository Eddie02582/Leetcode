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

## 思路DFS

## Code

#### Python

```python
class Solution(object):
    def hasPathSum(self, root: sum):        
       if not root: return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val)   
```


#### C++
```c++
class Solution {
public:

    bool hasPathSum(TreeNode* root, int targetSum) {   
        if (root == NULL)
            return false;
        targetSum ==  targetSum - root->val;
        if (root->left == NULL & root->right == NULL) 
            return targetSum == 0;  
        return hasPathSum(root->left,targetSum) || hasPathSum(root->right,targetSum);
    }
};
```




## 思路BFS

## Code

#### Python
```python
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        from collections import deque  
        if not root:
            return False

        queue = deque([root])    
        while queue:            
            node = queue.popleft()
            if not node.left and not node.right and node.val == targetSum:
                return True
            if node.left:
                node.left.val += node.val
                queue.append(node.left)
            if node.right:
                node.right.val += node.val
                queue.append(node.right)   
        return False
```

