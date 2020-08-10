class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0        
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
       
        val = 1
        for col in range(0,n):
            if obstacleGrid[0][col] == 1:
                val = 0
            obstacleGrid[0][col] = val

        val =  obstacleGrid[0][0]  
        for row in range(1,m):
            if obstacleGrid[row][0] == 1:
                val = 0
            obstacleGrid[row][0] = val     
            
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        
        return obstacleGrid[-1][-1]
                
    def uniquePathsWithObstacles_(self, obstacleGrid):
        if not obstacleGrid:
            return 0        
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] *(n + 1)  for i in range(m + 1)]
        
        for col in range(1,n + 1):
            if obstacleGrid[0][col - 1] == 0:
                dp[1][col] = 1
            else:
                break
            


        for row in range(1,m + 1):
            if obstacleGrid[row - 1][0] == 0:
                dp[row][1] = 1
            else:
                break
            
        
        for i in range(2,m + 1):
            for j in range(2,n + 1):
                if obstacleGrid[i - 1][j - 1] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m][n]

sol = Solution()

obstacleGrid = [
                [0,0,0],
                [0,1,0],
                [0,0,0]
            ]
sol.uniquePathsWithObstacles(obstacleGrid)


obstacleGrid = [
                [1,0,0],
                [0,1,0],
                [0,0,0]
            ]
sol.uniquePathsWithObstacles(obstacleGrid)