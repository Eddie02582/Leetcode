class Solution:
    def minPathSum_(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [ [0] * n  for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                if row == 0 and col != 0: 
            	    dp[row][col] = dp[row][col - 1] + grid[row][col]
                elif col == 0 :
            	    dp[row][col] = dp[row - 1][col] + grid[row][col]
                else:
                    dp[row][col] = min(dp[row][col - 1],dp[row - 1][col]) + grid[row][col]   

        return dp[-1][-1]      

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]    
    
sol = Solution()
sol.minPathSum(grid)
sol.minPathSum([[1,2,3,4]])