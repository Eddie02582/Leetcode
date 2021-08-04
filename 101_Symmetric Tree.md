# Symmetric Tree


## 原題目:
```
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
```

## 思路
1.遞回比較兩個root ,左邊等於右邊,右邊等於左邊




## Code

#### Python

``` python
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSame(t1,t2):
            return t1 and t2 and t1.val==t2.val and isSame(t1.left,t2.right) and isSame(t1.right,t2.left) or t1 is t2
        
        if root==None:
            return True
        return isSame(root.left,root.right)
        
```  

## BFS
每次將每一層加入隊列,並判斷每層是否對稱


``` python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        queue =[[root]]
        count = 1
        while queue:
            nodes = queue.pop()

            
            l ,r = 0 , len(nodes) - 1
            while l < r :
                if nodes[l] and not nodes[r]:
                    return False
                elif not nodes[l] and  nodes[r]:
                    return False
                elif not nodes[l] and  not nodes[r]:
                    pass
                elif nodes[l].val != nodes[r].val:
                    return False   
                l += 1
                r -= 1             
                
            layer = []
            for node in nodes:
                if node != None:
                    layer.append(node.left)
                    layer.append(node.right)
                
            if layer:
                queue.append(layer)        
        
        return True  
 ```



另一種思路,隊列的順序請由對稱入列

``` python
class Solution(object):
    def isSymmetric(self, root):  
        if not root:
            return True        
        elif not root.left and  not root.right:
            return True
        elif not root.right or not root.left:
            return False
                

        queue = [root.left,root.right]

        while queue:
            for i in range(len(queue)//2):
                root1 = queue.pop(0)
                root2 = queue.pop(0)
                if root1.val != root2.val:
                    return False
                if root1.left and not root2.right:
                    return False
                elif not root1.left and root2.right:
                    return False
                elif not root1.right and root2.left:
                    return False
                elif root1.right and not root2.left:
                    return False


                if root1.left:
                    queue.append(root1.left)
                    queue.append(root2.right)

                if root1.right:
                    queue.append(root1.right)
                    queue.append(root2.left)

        return True
 ```










