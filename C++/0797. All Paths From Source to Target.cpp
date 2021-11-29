#include<vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>>paths;       
        vector<int>path;      
        dfs(graph,paths,path,0);
        return paths;
        
    }   
    void dfs(vector<vector<int>>& graph,vector<vector<int>>& paths,vector<int> &path,int n) {
        path.push_back(n);        
        if(n == graph.size() - 1 ){
            paths.push_back(path);           
        }      
       
        for(auto i: graph[n]){  
           dfs(graph,paths,path,i);               
                 
        }     
        path.pop_back();         
    }
};

