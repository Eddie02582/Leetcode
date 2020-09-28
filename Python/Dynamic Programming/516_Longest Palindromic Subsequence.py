class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        n = len(s)
        dp = [ [0] * n for _ in range(len(s))]
        
        for i in range(n - 1, -1,-1):
            for j in range(i,n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max (dp[i][j - 1],dp[i + 1][j])
        
        print (dp)
        return dp[0][-1]
                
               
               
sol = Solution()
sol.longestPalindromeSubseq('bbbab')