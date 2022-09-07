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
        if(!root)        
            return false;
        targetSum -= root->val;
        if (!root->right && !root->left)
            return targetSum == 0;       
        return  hasPathSum(root->left,targetSum) || hasPathSum(root->right,targetSum);
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