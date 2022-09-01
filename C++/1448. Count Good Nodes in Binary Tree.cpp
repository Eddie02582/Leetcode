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
    int goodNodes(TreeNode* root) {   
        return dfs(root,root->val);
    }
    
    int dfs(TreeNode* root,int maxValue){
        if (!root)
            return 0;        
        if (root->val >= maxValue){
            maxValue = root->val;
            return dfs(root->left,maxValue) + dfs(root->right,maxValue) + 1;
        }
        else{
            return dfs(root->left,maxValue) + dfs(root->right,maxValue);
        }  
    }   

    int goodNodes_bfs(TreeNode* root,int maxValue){
        if (!root)
            return 0; 
        
        int good = 1;
        queue<TreeNode*> q;
        q.push(root);
        
        while(!q.empty()){
            int size = q.size();
            for(int i = 0; i < size;i++){
                TreeNode *node = q.front(); 
                q.pop();
                if(node->left){
                    if(node->left->val >= node->val){
                        good++;                        
                    }      
                    else{
                        node->left->val = node->val;
                    }
                    q.push(node->left);
                }
                if(node->right){
                    if(node->right->val >= node->val){
                        good++;                        
                    }      
                    else{
                        node->right->val = node->val;
                    }
                    q.push(node->right);
                }                    
            }   
        }        
        return good;
    }     
    
};








