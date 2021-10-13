#include<vector>
#include<string>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<bool>visited(nums.size(),false);
        vector<vector<int>> ans;
        vector<int> path;
        backtracking(nums,ans,path,visited);
        return ans;
        
    }

    void backtracking(const vector<int>& nums,vector<vector<int>> &ans,vector<int>& path,vector<bool>& visited){
        
        if(path.size() == nums.size()){
            ans.push_back(path);
            return ;
        }

        for(int i = 0;i<nums.size();i++)
        {
            if(!visited[i]){
                visited[i] = true;
                path.push_back(nums[i]);
                backtracking(nums,ans,path,visited);
                visited[i] = false;
                path.pop_back();
            }
        }
    }

    // []
    // [1]
    // [1,2],[2,1]
    // [3,1,2],[1,3,2],[1,2,3],[3,2,1],[2,3,1],[2,1,3]
    vector<vector<int>> permute2(vector<int>& nums) {        
        vector<vector<int>> ans;
        ans.push_back(vector<int> {nums[0]});        

        for(int i = 1; i <nums.size();i++){
            int size = ans.size();
            vector<vector<int>> temp;
            for (int j = 0;j<size;j++){  
                for (int k = 0; k < ans[j].size() + 1;k++){
                    vector<int> sub (ans[j]);
                    sub.insert(sub.begin() + k,nums[i]);                    
                    temp.push_back(sub);                
                }
            };
            ans = temp;
        }
        return ans;        
    }


    void permute3(vector<vector<int>> &ans,int idx, vector<int> &arr){
        if(idx == arr.size()-1){
            ans.push_back(arr);
            return;
        }
        for (int i = idx; i < arr.size();i++){
            swap(arr[i], arr[idx]);
            permute3(ans, idx + 1, arr);
            swap(arr[i], arr[idx]);
        }

    }
    vector<vector<int>> permute3(vector<int>& arr) {
        vector<vector<int>> ans;
        permute3(ans, 0, arr);
        return ans;
    }


};

int main(){
    Solution sol;
    vector<int> nums ({1,2,3});
    sol.permute3(nums);

}