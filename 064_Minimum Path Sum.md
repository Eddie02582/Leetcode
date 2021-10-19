# Minimum Path Sum

## 原題目:
```
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

## 思路
典型的dp,每一個一定是從左方或上方來,dp[i][j] = min(dp[i - 1][j],dp[i][j - 1]),但是要注意邊界

#### Python

``` python
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
``` 

這邊的話先處理邊界的問題

``` python
class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        for col in range(1,n):
            grid[0][col] += grid[0][col - 1]

        for row in range(1,m):
            grid[row][0] += grid[row - 1][0]

        
        for row in range(1,m):
            for col in range(1,n):  
                grid[row][col] = min(grid[row][col - 1],grid[row - 1][col]) + grid[row][col]   

        return dp[-1][-1]  
``` 

#### C++

```c++
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<int> dp(n,0);
        
        
        for (int i = 0;i < m;i++){
            for(int j = 0;j < n;j++){                 
                if(j == 0 && i == 0){
                    dp[j] = grid[i][j];
                }
                else if(i == 0){
                    dp[j] = grid[i][j] +dp[j - 1];
                }
                else if(j == 0){
                    dp[j] += grid[i][j];                 
                }
                else{
                    dp[j] = grid[i][j] + min(dp[j],dp[j- 1]);                                 
                }  
            }  
                  
        }
        return dp[n - 1];  
    }
};
```
