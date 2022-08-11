# Unique Binary Search Trees


## 原題目:
```
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

## 思路

## Code

#### C++


```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if(root == NULL)
            return true;           
        return checkBST(root->left,0,root->val) && checkBST(root->right,1,root->val);
    }
    bool checkBST(TreeNode* root,int mode,int value){
        if(root == NULL)
            return true;
        if (mode == 0 && root->val >= value)
            return false;
        else if (mode == 1 && root->val <= value)
            return false;    
        
        return checkBST(root->left,0,min(root->val,value)) && checkBST(root->right,1,max(root->val,value));        
    }
    
};





```
















