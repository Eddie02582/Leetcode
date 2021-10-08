#include <iostream>
#include <vector>

using namespace std;

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
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == NULL)
            return {};

        vector<int> ans ;
        traverse(root,ans);
        return ans;
        
    }
    
    void traverse(TreeNode* root,vector<int> &ans ) {
        if (root == NULL)
            return ;   
        traverse(root->left,ans);
        ans.push_back(root->val);
        traverse(root->right,ans);        
    } 

    vector<int> inorderTraversal2(TreeNode* root) 
    {
        stack<TreeNode*> stk ; 
        vector<int> inorder ;
        TreeNode* node = root ;
        
        while(true)
        {   
            if(node != NULL)
            {
                stk.push(node); 
                node = node->left ;
            }
            else{
                if(stk.size() == 0)
                    break ;
                node = stk.top() ; 
                stk.pop() ;
                inorder.push_back(node->val);
                node = node->right ;
            }
               
        }
        return inorder;
    }
    
};


int main()
{

}