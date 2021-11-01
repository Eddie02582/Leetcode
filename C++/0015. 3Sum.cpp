#include<algorithm>
#include<vector>

using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>>  ans;  
        if (nums.size() <3)
            return ans;
        sort(nums.begin(),nums.end());
           
        
        for (int i = 0;i < nums.size() - 1;i++){
            if ( i >0 && nums[i] == nums[i - 1])
                continue;            
            int left = i + 1,right = nums.size() - 1;           
            while (left < right){
                int total = nums[left] + nums[right] + nums[i];
                if(total == 0){
                    ans.push_back(vector<int>{nums[i],nums[left],nums[right]});
                    left += 1;
                    right -= 1;
                    while (left < right && nums[left] == nums[left - 1])
                        left += 1;                    
                    while (left < right && nums[right] == nums[right + 1])
                        right -= 1;
                                    
                }
                else if (total < 0)
                    left += 1;
                else
                    right -= 1;
                
            }
        }   
        return ans; 
    }
};

