
#include<queue>
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
    int sumNumbers(TreeNode* root,int val = 0) {
        if (root == nullptr)
            return 0;  

        val = val * 10 + root->val;
        if (root->left ==  nullptr && root->right ==  nullptr)   
            return val       
        
        return sumNumbers(root->left,val) + sumNumbers(root->right,val);
    }

    int sumNumbers_bfs(TreeNode* root,int val = 0) {
        if (root == nullptr)
            return 0;  

        queue <TreeNode*> q;
        q.push(root);
        int total;
        while (!q.empty()){
            int size = q.size();
            for (int i = 0;i < size();i++){
                TreeNode* node = q.front();
                q.pop();
                if(node->left != nullptr){
                    node->left->val = node->val * 10  + node->left->val; 
                    q.push(node->left);
                }
                if(node->right != nullptr){
                    node->right->val = node->val * 10  + node->right->val; 
                    q.push(node->left);
                }
                if(node->right == nullptr && node->left == nullptr)
                    total += node->val;
            }
        }       
        
        return total;
    }
};

