// Your First C++ Program

#include <iostream>
#include <vector> 
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int size = nums.size();        
        vector<int> dp(size + 1, 0);
         dp[1] = nums[0];
        for (int i = 2;i <= size; i ++){            
            dp[i] = max(dp[i - 1],dp[i - 2] + nums[i - 1]);
        }        
        return dp[size];
    }
};


int main() {
    vector<int> nums({1,2,3,1 });
	Solution sol;
	sol.rob(nums);
}