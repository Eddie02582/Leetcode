#include<vector>

using namespace std;

class Solution {
public:

    vector<vector<int>> ans;
    vector<vector<int>> findSubsequences(vector<int>& nums) {    
        vector<int> path;
        backtracking(nums,path,0);
        return ans;
        
    }
    
    void backtracking(vector<int>& nums,vector<int>& path,int start){    
        if(start == nums.size())
            return ;        
        if(path.size() >= 2)            
            ans.push_back(path);  
            
        if( path.empty() || nums[start] >= path[path.size()- 1]){
            path.push_back(nums[start]);
            backtracking(nums,path,start + 1);
            path.pop_back();
        }
        backtracking(nums,path,start + 1);             
        
        
    }
    
    
    
};