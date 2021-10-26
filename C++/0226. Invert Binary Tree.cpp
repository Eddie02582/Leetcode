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
    TreeNode* invertTree(TreeNode* root) { 
        if (root == nullptr)
            return root;
        TreeNode* right = invertTree(root->right);
        TreeNode* left = invertTree(root->left);
        root->left = right;
        root->right = left;
        return root;
    }

    TreeNode* invertTree_(TreeNode* root) {     
        invertTree_dfs(root);
        return root;
    }
    void invertTree_dfs(TreeNode* root) {
        if (root == nullptr)
            return ;
        
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;        
        
        invertTree_dfs(root->left);       
        invertTree_dfs(root->right);
    }
};