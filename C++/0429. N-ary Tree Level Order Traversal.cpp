/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ans;
        dfs(root,0,ans);
        return ans;
    }     
    
    void dfs(Node* root,int level,vector<vector<int>> &ans){
        if (!root)
            return;       
        if (ans.size() == level){ 
            ans.push_back(vector<int>{});
        }        
        ans[level].push_back(root->val);
        
        for(auto &child : root->children){           
            dfs(child,level + 1,ans);
        } 
    }
    
    vector<vector<int>> levelOrder_bfs(Node* root) { 
        vector<vector<int>> ans;
        if(!root)
            return ans;
        queue<Node*>q;
        q.push(root);
        int level = 0;
        while(!q.empty()){
            int size = q.size();
            vector<int> level_val;
            for(int i = 0;i<size;i++){
                Node* node = q.front();
                q.pop();
                level_val.push_back(node->val);
                for(auto &child : node->children){
                    q.push(child);
                }                
            }
            ans.push_back(level_val);
            level++;            
        }        
        return ans;
    } 
    
    
    
    
};












