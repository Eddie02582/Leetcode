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
        if n < 4:
            return n

        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4,n+1):
            for j in range(1,int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
                
        return dp[-1]



sol = Solution()
sol.numSquares(12)

