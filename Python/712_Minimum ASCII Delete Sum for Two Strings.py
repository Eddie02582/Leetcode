class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:   
        m,n = len(s1),len(s2)
        dp = [ [0] * (m + 1)  for _ in range(n + 1)]
        
        for i in range(1,n + 1):
            dp[i][0] = dp[i - 1][0] + ord(s2[i - 1])
            
        for j in range(1,m + 1):
            dp[0][j] = dp[0][j - 1] +ord(s1[j - 1])        
        
        for i in range(1,n + 1):
            for j in range(1,m + 1):                                
                if s1[j - 1] == s2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    d1 = dp[i - 1][j - 1] + ord(s2[i - 1]) + ord(s1[j - 1])
                    d2 = dp[i][j - 1] + ord(s1[j - 1])
                    d3 = dp[i - 1][j] + ord(s2[i - 1])                    
                    dp[i][j] = min(d1,d2,d3)               
        
       
        return dp[n][m]