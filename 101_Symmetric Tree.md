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
nums2 放入nums1 排序即可,底下用汽泡排序法排

``` python
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSame(t1,t2):
            return t1 and t2 and t1.val==t2.val and isSame(t1.left,t2.right) and isSame(t1.right,t2.left) or t1 is t2
        
        if root==None:
            return True
        return isSame(root.left,root.right)
        
```  




















