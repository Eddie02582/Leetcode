class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp = [False] * (N+1)        
        for i in range(2, N+1):            
            for k in range(1, i):
                if i % k == 0 and not(dp[i-k]):                    
                    dp[i] = True
        return dp[N]       