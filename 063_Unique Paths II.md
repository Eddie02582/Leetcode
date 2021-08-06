# Unique Paths

## 原題目:
```
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


```


## 思路 dp



``` python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [ [0] *n for _ in range(m)]
        
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]
``` 






## 思路 dp inplace



#### Python

``` python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0        
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
       
        val = 1
        for col in range(n):
            if obstacleGrid[0][col] == 1:
                val = 0
            obstacleGrid[0][col] = val

        val =  obstacleGrid[0][0]  
        for row in range(m):
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
``` 
