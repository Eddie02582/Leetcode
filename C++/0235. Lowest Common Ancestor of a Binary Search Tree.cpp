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
    
    TreeNode* lowestCommonAncestor_simple(TreeNode* root, TreeNode* p, TreeNode* q) {
        if ( (root->val - p->val) *  (root->val - q->val) <= 0 )
            return root;      
        else if (p->val > root->val)
            return lowestCommonAncestor(root->right,p,q);
        else
            return lowestCommonAncestor(root->left,p,q);
    }
    
};