class Solution:
    def numSquares_(self, n):
        if n <= 0:
            return 0
    
        squares = [ i * i for i in range(int(n**0.5) + 1)]
        
        dp = [ [ float("inf")] * (n + 1) for _ in range(len(squares))]        
        for i in range(1,len(squares)):            
            for j in range(1,n + 1):
                if j > squares[i]:
                    dp[i][j] = min(dp[i - 1][j],dp[i][j - squares[i]] + dp[i][squares[i]])  
                elif j == squares[i]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp

    def numSquares(self, n: int) -> int:
        coins = [ i * i for i in range(1, int(n**0.5) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
    
        for i in range(1, n + 1):
            dp[i] = min([1 + dp[i - coin] for coin in coins])          
        return dp[-1]   


sol = Solution()
sol.numSquares(12)

