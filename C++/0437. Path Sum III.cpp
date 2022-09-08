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
    int count = 0;
    int pathSum(TreeNode* root, int targetSum) {
        vector<long> sums;
        dfs(root,sums, targetSum);
        return count;
    }
    void dfs(TreeNode* root,vector<long> sums, int targetSum){
        if (!root)
            return;       
        
        if(root->val == targetSum)
             count += 1;
        for (int i = 0;i < sums.size();i++){   
            sums[i] += root->val;
            if (sums[i] == targetSum)
                count += 1;                  
        }       
        sums.push_back(root->val);
        if(root->left){
            dfs(root->left,sums, targetSum);
        }
        if(root->right){
            dfs(root->right,sums, targetSum);  
        }   
        sums.pop_back();
        for (int i = 0;i < sums.size();i++){     
            sums[i] -= root->val;
        }
    }
};
