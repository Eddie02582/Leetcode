// Your First C++ Program

#include <iostream>
#include <vector> 
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int size = nums.size();
        if (size == 0) return 0;
        if (size == 1) return nums[0];        
        // dp[i] represents the maximum amount of money we can rob up to house i
        vector<int> dp(size + 1, 0);
        
        dp[1] = nums[0];  // Robbing the first house        
        // Start filling the dp array from the second house
        for (int i = 2; i <= size; ++i) {
            // dp[i] = max of not robbing this house (dp[i-1]) or robbing this house (dp[i-2] + nums[i-1])
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1]);
        }        
        return dp[size];  
    }
};


int main() {
    vector<int> nums({1,2,3,1 });
	Solution sol;
	sol.rob(nums);
}