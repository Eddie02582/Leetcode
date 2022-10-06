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
 #include <algorithm>
 #include <climits>
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if(!root)
            return true;           
        return checkBST(root,LONG_MIN,LONG_MAX);
    }
    bool checkBST(TreeNode* root,long lower,long upper){
        if(!root)
            return true;
        if  (root->val >= upper || root->val <= lower)
            return false;   
        
        return checkBST(root->left,lower,root->val) && checkBST(root->right,root->val,upper);        
    }   
    
};


