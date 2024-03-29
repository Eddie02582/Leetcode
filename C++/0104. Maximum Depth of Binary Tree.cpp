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
    int maxDepth(TreeNode* root) {
        if (!root)
            return 0;          
        return max(maxDepth(root->left),maxDepth(root->right)) + 1 ;
    }
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        int maxLeft = maxDepth(root->left);
        int maxRight = maxDepth(root->right);
        return max(maxLeft, maxRight)+1;
    }
        
    
    int maxDepth_bfs(TreeNode* root) {
        if (!root)
            return 0;
        int depth = 0;
        queue<TreeNode*> q;
        q.push(root);        
        while(!q.empty()){
            int size = q.size();           
            for (int i = 0;i < size;i++){
                TreeNode* node = q.front();
                q.pop();
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right);              
            }
            depth++;
            
        }
        return depth;
    }
    
    
};