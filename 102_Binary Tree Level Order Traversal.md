# Binary Tree Level Order Traversal


## 原題目:
```
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
       
return its level order traversal as:
    [
      [3],
      [9,20],
      [15,7]
    ]
```

## 思路1 
此題爲廣度優先搜索(BFS)的基礎題，使用一個隊列保存每層的節點即可。出隊列和將子節點入隊列的實現
使用 for 循環，將每一輪的節點輸出。




## Code

#### Python

``` python
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        queue = []
        queue.append(root)
        output = []
        
        while len(queue) > 0:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop(0)
                
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
                    
                level.append(node.val)
                
            output.append(level)
            
        return output
        
```  




## 思路2
使用preorder 概念,但是多了level 參數記錄所在層數




## Code

#### Python

``` python
class Solution(object):
    def levelOrder(self, root):
        import collections
        self.dp = collections.defaultdict(list)
        def next_level(node,level):
            if node is None:
                return 
            self.dp[level].append(node.val)
            next_level(node.left, level+1)  
            next_level(node.right, level+1)  
         
        next_level(root, 0) 
        return self.dp.values()

```  


``` python
class Solution(object):
    def levelOrder(self, root) :
        self.res = []
        self.level_scan(root, 1)
        return self.res
    
    def level_scan(self, node, level):
        
        if node:
            if len(self.res) < level:
                self.res.append([])
            self.res[level-1].append(node.val)
        else:
            return
        if node.left:
            self.levelOrder(node.left, level+1)
        if node.right:
            self.levelOrder(node.right, level+1)
```  
















