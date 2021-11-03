#include<unordered_map>
#include<vector>

class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int,int> counts;
        for (int num : nums){
            counts[num]++;
        }
       
        vector<int> ans;
        for(auto it = counts.begin();it!= counts.end();it ++){
            if (it->second > nums.size()/3)
                ans.push_back(it->first);            
        }
        return ans;
    }
};