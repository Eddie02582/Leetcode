class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m,n = len(A),len(B)
        dp = [ [0]*(m + 1) for _ in range(n + 1)]
        
        for i in range(1,n + 1):
            for j in range(1,m + 1):
                if B[i - 1] == A[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j - 1],dp[i][j - 1],dp[i - 1][j])          
        return dp[n][m]