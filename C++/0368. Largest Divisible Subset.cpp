class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {        
        int max_sub_loc = 0;
        vector<vector<int>> dp (nums.size(),vector<int>{});
        sort(nums.begin(), nums.end());

        for (int i = 0;i < nums.size();i++){
            int loc = -1,sub_size = -1;
            for (int j = 0;j < i; j++){
                int size = dp[j].size();    
                if(size == 0 || nums[i] % dp[j][size - 1] == 0 ){
                    if(size > sub_size){
                        loc = j;
                        sub_size = size;
                    }
                }                
            }
  
            if(loc >= 0)
                dp[i].assign(dp[loc].begin(),dp[loc].end());

            dp[i].push_back(nums[i]);

            if(dp[i].size() >dp[max_sub_loc].size()){
                max_sub_loc = i;               
            }

        }
      
        return dp[max_sub_loc];
    }
};
