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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root)
            return new TreeNode(val);
        
        queue<TreeNode*> q;
        q.push(root);        
        while(!q.empty()){
            TreeNode* node = q.front();
            q.pop();
            if(val > node->val){
                if(node->right)
                    q.push(node->right);                
                else
                    node->right = new TreeNode(val);                
            }
            else if(val < node->val){
                if(node->left)
                    q.push(node->left);                
                else
                    node->left = new TreeNode(val);                
            }                 
        } 
        return root; 
    }
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(!root)
            return new TreeNode(val);
        if(val > root->val){
            root->right = insertIntoBST(root->right,val);
        }
        else{
            root->left = insertIntoBST(root->left,val);
        }
        return root;
    }
    
};