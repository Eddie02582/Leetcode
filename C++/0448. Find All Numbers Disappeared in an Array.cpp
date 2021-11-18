#include<vector>
#include<unordered_set>

using namespace std;
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) { 
        vector<int> ans;         
        unordered_set<int> exist(nums.begin(), nums.end());        

        for (int i = 1;i <= nums.size();i++){
            if(exist.count(i) == 0 ){
                ans.push_back(i);                
            }            
        }       
        return ans;
    }
    }
    
    vector<int> findDisappearedNumbers_(vector<int>& nums) {
        vector<int> ans;
        vector<bool> exist(nums.size() + 1);       
        
        for (auto num :nums){
            exist[num] = true;
        }
        for (int i = 1;i < exist.size();i++){
            if(!exist[i]){
                ans.push_back(i);                
            }            
        }       
        return ans;
    }
};