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

#include <cstddef>

  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };


class Solution {
public:

    bool hasPathSum(TreeNode* root, int targetSum) {   
        if (root == NULL)
            return false;
        targetSum ==  targetSum - root->val;
        if (root->left == NULL & root->right == NULL) 
            return targetSum == 0;  
        return hasPathSum(root->left,targetSum) || hasPathSum(root->right,targetSum);
    }


    bool hasPathSum2(TreeNode* root, int targetSum) {   
        return dfs(root,targetSum);
    }
    
    bool dfs(TreeNode* root, int targetSum)
    {   
        if (root == NULL)
            return false;
        targetSum ==  targetSum - root->val;
        if (root->left == NULL & root->right == NULL)        
            return targetSum == 0;             
        return dfs(root->left,targetSum) || dfs(root->right,targetSum);
    }
};



int main()
{
    Solution sol;
    TreeNode* root = new TreeNode(1);
    TreeNode* left = new TreeNode(2);
    root->left = left;
    sol.hasPathSum(root,1);
}