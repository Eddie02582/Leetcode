class Solution:
    def numDecodings(self, s: str) -> int:    
        dp = {}
        if s[0] == '0':
            return 0      
        dp[-1] = 1             
        dp[0] = 1

        for i in range(1,len(s)):
            if s[i] == "0":
                if  1 <= int(s[i - 1])<=2:
                    dp[i] = dp[i - 2]                
                else:
                    return 0
            else:
                if 10 <= int(s[i - 1: i + 1]) <= 26:
                    dp[i] = dp[i - 2] + dp[i - 1]               
                else :  
                    dp[i] = dp[i - 1] 

        return dp[len(s) - 1]
```  