#include <vector>
using namespace std;
class Solution {
public:
    int jump(vector<int>& nums) {
        int size = nums.size();
        vector<int> dp(size,INT_MAX);
        dp[0] = 0;
        for(int i = 0;i < size;i++){  
            int loc = i + 1;
            while (loc <= i + nums[i] && loc < size){                
                dp[loc++] = min(dp[i] + 1,dp[loc]) ; 
                loc++;
            } 
        }        
        return dp[size - 1];  
    }
};