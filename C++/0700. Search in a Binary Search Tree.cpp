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
    TreeNode* searchBST(TreeNode* root, int val) {
        if (!root)
            return NULL;
        if(val == root->val)
            return root;
        else if(val > root->val)
            return searchBST(root->right,val);
        else
            return searchBST(root->left,val);
    }
    
    TreeNode* searchBST_(TreeNode* root, int val) {
        queue<TreeNode*> q;
        q.push(root);        
        while(!q.empty()){
            TreeNode* node = q.front();
            q.pop();
            if(node->val == val)
                return node;
            if(val > node->val && node->right)
                q.push(node->right);
            else if(node->left)
                q.push(node->left);            
        }      
        
        return NULL;
    }
    
};