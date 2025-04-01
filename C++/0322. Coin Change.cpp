class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, INT_MAX);		
		dp[0] = 0;

		for(int coin:coins){			
			for(int i = coin;i<= amount;i++){
				if(dp[i - coin] != INT_MAX){
					dp[i] = min(dp[i - coin] + 1,dp[i]);
				}
			}		
		}
		return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
	
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, INT_MAX);  
        dp[0] = 0;         
        // 遍历每个金额
        for (int i = 1; i <= amount; ++i) {
            // 对每个硬币
            for (int coin : coins) {
                if (i >= coin && dp[i - coin] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);  // 选择最小的硬币数
                }
            }
        }

        // 如果 dp[amount] 还是 INT_MAX，说明无法构造金额
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
};
