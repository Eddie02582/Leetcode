# Lowest Common Ancestor of a Binary Search Tree


## 原題目:
```
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

      6
    /   \
   2     8
  / \   / \
 0   4 7   9
    / \
   3   5
   
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.
   
Example 2:
      6
    /   \
   2     8
  / \   / \
 0   4 7   9
    / \
   3   5

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition. 
   
Example 3:
    Input: root = [2,1], p = 2, q = 1
    Output: 2
 
Constraints:
The number of nodes in the tree is in the range [2, 105].
    -10**9 <= Node.val <= 10**9
    All Node.val are unique.
    p != q
    p and q will exist in the BST.

 
```

## 思路 
```
      6
    /   \
   2     8
  / \   / \
 0   4 7   9
    / \
   3   5
```

因為為BST,所以LCA的節點(L)，只有2種狀況：<br> 
1.L是p或q其中之一的話，遇到誰，就代表誰是那個LCA。<br>   
2.L不是p或q其中之一的話，L的値的範圍必在p.val和q.val之間<br> 
```
從root開始,有幾種情況
1.當root 等於p 或是等於q 回傳root
2.當root 值介於p~q之間回傳root
3.p和q的値都小於root的值 => 往下找root.left
4.p和q的値都大於root的值 => 往下找root.right
```
以(4,5)為例
```
1.(4,5)皆比6小,代表L會存在6的左邊
2.(4,5)皆比2大,代表L會存在2的右邊
3.4剛好等於p 即為LCA的節點
```




#### C++
``` c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == p || root == q)
            return root;
        else if (p->val < root->val && q->val > root->val)
            return root;
        else if (p->val > root->val && q->val < root->val)
            return root;     
        else if (p->val > root->val && q->val > root->val)
            return lowestCommonAncestor(root->right,p,q);
        else
            return lowestCommonAncestor(root->left,p,q);
    }      
};


``` 

簡化當root值介在pq之間, 表示(root->val - p->val) *  (root->val - q->val) <= 0 ,即可簡化


``` c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if ( (root->val - p->val) *  (root->val - q->val) <= 0 )
            return root;      
        else if (p->val > root->val)
            return lowestCommonAncestor(root->right,p,q);
        else
            return lowestCommonAncestor(root->left,p,q);
    }
    
};


``` 







