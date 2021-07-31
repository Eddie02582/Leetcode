#  Number of Islands


## 原題目:
```
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:
	Input: grid = [
	  ["1","1","1","1","0"],
	  ["1","1","0","1","0"],
	  ["1","1","0","0","0"],
	  ["0","0","0","0","0"]
	]
	Output: 1
	
Example 2:
	Input: grid = [
	  ["1","1","0","0","0"],
	  ["1","1","0","0","0"],
	  ["0","0","1","0","0"],
	  ["0","0","0","1","1"]
	]
	Output: 3
	 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
```

## 思路DFS
迴圈作&運算,會TLE


#### Python

``` python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x,y):  
            grid[x][y] = "*"           
            for r,c in [(x + 1,y),(x - 1,y),(x,y - 1),(x, y+ 1)]:
                if 0 <= r < m and 0<= c <n and grid[r][c] == "1":                    
                    dfs(r,c)

        m,n = len(grid),len(grid[0])
        num_island = 0 
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":                   
                    dfs(x,y)                    
                    num_island += 1        
        return num_island 
``` 

## 思路BFS

