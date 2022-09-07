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
    vector<vector<int>> paths;
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        dfs(root, path,targetSum);   
        return paths;
    }
    
    void dfs(TreeNode* root, vector<int> &path,int targetSum){
        if (!root)
            return ;       
        path.push_back(root->val);
        targetSum -= root->val;
        
        if (!root->left && !root->right && targetSum == 0){            
            paths.push_back(path);  
        }
        if(root-> left){            
            dfs(root-> left,path,targetSum);        
        }
        if(root-> right)
        {               
            dfs(root-> right,path,targetSum); 
        }
        path.pop_back();    
    }
    
};