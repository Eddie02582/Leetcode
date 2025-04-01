class Solution {
public:
	/*dp[i] 表示以 nums[i] 作为末尾的最长递增子序列的长度。

	對於每個 nums[i]，遍歷它之前的所有元素 nums[j]（j 從 0 到 i-1）
	。如果 nums[j] < nums[i]，表示 nums[i] 可以接在 nums[j] 後面組成一個較長的遞增子序列。
	因此，更新 dp[i] = max(dp[i], dp[j] + 1)。
	*/
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n,1);
        int maxLength = 1;
        for( int i = 0; i < n;i++){            
            for(int j = 0; j <i;j++){
                if(nums[j] < nums[i]){
                    dp[i] = max(dp[i], dp[j] + 1) ;                   
                }
            }               
            maxLength = max(dp[i], maxLength) ;  
        }
        return maxLength;
        
    }
	/*
	這個方法是從後往前的動態規劃。 LIS[i] 表示從 nums[i] 開始的最長遞增子序列的長度。
	對於每個 nums[i]，遍歷它後面的所有元素 nums[j]（j 從 i+1 到 n-1）。
	如果 nums[i] < nums[j]，表示 nums[i] 可以接在 nums[j] 前面組成一個較長的遞增子序列
	因此，更新 LIS[i] = max(LIS[i], 1 + LIS[j])。
    */
    int lengthOfLIS2(vector<int>& nums) {
        vector<int> LIS(nums.size(), 1);

        for (int i = nums.size() - 1; i >= 0; i--) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] < nums[j]) {
                    LIS[i] = max(LIS[i], 1 + LIS[j]);
                }
            }
        }
        return *max_element(LIS.begin(), LIS.end());
    }	
	
};