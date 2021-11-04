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
    int sumOfLeftLeaves_bfs(TreeNode* root) {
        int total = 0;
        if (root == nullptr)
            return 0;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty()){            
            int size = q.size();
            for (int i = 0;i < size ;i++){                
                TreeNode* node = q.front();
                q.pop();                
                if(node->left != nullptr){
                    if(node->left->right == nullptr && node->left->left == nullptr){
                        total += node->left->val;
                    }     
                    else
                        q.push(node->left);                  
                }
                if(node->right != nullptr){                    
                    q.push(node->right);
                }
            }
            
        }
        return total;
    }
    
    int sumOfLeftLeaves_dfs(TreeNode* root) {
        int total = 0;
        if (root == nullptr)
            return 0;
        
        int left = 0;
        int right = 0;
        
        if(root->left != nullptr){
            if(root->left->right == nullptr && root->left->left == nullptr)
                left += root->left->val;            
            else
                left += sumOfLeftLeaves_dfs(root->left);            
        }
        if(root->right != nullptr)
           right += sumOfLeftLeaves_dfs(root->right);       
       
        return left + right;  
    }
    int sumOfLeftLeaves(TreeNode* root,int direction = -1) {
      
        if (root == nullptr)
            return 0;       
        
        if (root->left == nullptr && root->right == nullptr)             
            return direction == 0 ? root->val : 0;

        int left  = sumOfLeftLeaves(root->left, 0); // 0 means left direction
        int right = sumOfLeftLeaves(root->right, 1); // 1 means right direction          
        return left + right;  
        
        
    }
    
    
    
    
    
    
    
    
    
    
};