
 struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}

 }
 
 
#include <iostream>
#include <queue> 
#include <unordered_map> 
using namespace std;

class Solution {

public:

    bool isCousins(TreeNode* root, int x, int y) {
        
        queue<TreeNode*> q ;
        unordered_map<int,int> parent ;
       
        q.push(root);        
        while (!q.empty()){
            int size = q.size();
            for (int i = 0; i <size;i++){
                TreeNode* node = q.front();
                q.pop();
                if (node->left != nullptr){
                    parent[node->left->val] = node->val;
                    q.push(node->left);
                }
                if (node->right != nullptr){
                    parent[node->right->val] = node->val;
                    q.push(node->right);
                }               
            }
            if (parent.count(x) && parent.count(y)){
                if(parent[x] != parent[y] ){
                    return true;
                }
                else{
                    return false;
                }
            }
            else if (parent.count(x) || parent.count(y)) {
                return false;
            }           
        }
        return false;       
        
    }    


};