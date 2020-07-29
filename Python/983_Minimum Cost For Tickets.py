class Solution:    
    def mincostTickets(self, days, costs):
        dp = [0] * (days[- 1] + 1)
        
        exist = set(days)

        
        for i in range(1,len(dp)):
            if i in exist: 
                if i <= 7:
                    dp[i] = min(dp[i - 1] + costs[0],costs[1],costs[2])
                elif i <= 30:
                    dp[i] = min(dp[i - 1] + costs[0],dp[i - 7] + costs[1],costs[2])
                else:
                    dp[i] = min(dp[i - 1] + costs[0],dp[i - 7] + costs[1],dp[i - 30] + costs[2])
            else: 
                dp[i] = dp[i - 1]     
        return dp[-1]   