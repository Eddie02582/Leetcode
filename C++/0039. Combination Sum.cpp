// Your First C++ Program

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>ans;
        vector<int>path;
        if(candidates.empty())
            return ans;

        backtracking(candidates,0,ans,path,target);        
        return ans;
    }
    
    void backtracking(vector<int>& candidates,int index,vector<vector<int>>& ans,vector<int>& path,int target){
        if (target == 0 )
        {
            ans.push_back(path);           
            return ;
        }
        else if (target < 0)
            return; 

        for (int i = index; i < candidates.size(); i++){
            //choose
            path.push_back(candidates[i]);
            backtracking(candidates,i,ans,path,target - candidates[i]);
            path.pop_back();
        }  
    }
    
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>>ans;
        vector<int>path;
        if(candidates.empty())
            return ans;

        backtracking2(candidates,0,ans,path,target);        
        return ans;
    }
    
    void backtracking2(vector<int>& candidates,int index,vector<vector<int>>& ans,vector<int>& path,int target){
        if (target == 0 )
        {
            ans.push_back(path);           
            return ;
        }
        else if (target < 0)
            return; 
        else if (candidates.size() == index)
            return; 
        int n = candidates[index];
        path.push_back(n);
        backtracking(candidates,index,ans,path,target - n );
        path.pop_back();
        backtracking(candidates,index + 1,ans,path,target );

    }


    
};


int main() {
    vector<int> nums({2,3,6,7});
	Solution sol;
	sol.combinationSum(nums,7);
}