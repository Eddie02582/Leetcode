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
    string tree2str(TreeNode* root) {
        if (!root)
            return "";
        if (root-> left && root->right)
            return to_string(root->val) + "("  + tree2str(root->left) + ")"+  "("+ tree2str(root->right) +  ")";
        else if (root->left)
            return to_string(root->val) + "("  + tree2str(root->left) + ")";
        else if (root->right)
            return to_string(root->val) + "()"+"("+ tree2str(root->right) +  ")";    
        else
            return to_string(root->val) ;
    }
    
    string tree2str_simple(TreeNode* root) {
        if (!root)
            return "";
        string s = to_string(root->val);
        
        if (root->left)
            s+= "("  + tree2str(root->left) + ")";
        else if (root->right)
            s+= "()" ;
        if (root->right)    
            s+="("+ tree2str(root->right) +  ")";
        return s ;
    }
    
};