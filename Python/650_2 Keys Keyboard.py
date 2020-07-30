class Solution:
    def minSteps(self, n):
        dp = [ i for i in range(n + 1)]
        dp[1] = 0
        
        for i in range(2,n// 2 + 1):
            p = 2 * i
            while p <= n:              
                dp[p] = min(dp[p],dp[i] + 1 + (p - i)//i)                
                p += i
        return dp[-1]
