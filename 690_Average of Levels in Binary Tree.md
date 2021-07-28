# Max Area of Island


## 原題目:
```
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
 
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50. 
 
```

## 思路bfs



#### Python
``` python
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #bfs
        from collections import deque        
        m,n = len(grid),len(grid[0])
        max_area = 0
        visited = {}
        lands = []
        
        #get land
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    lands.append([i,j])
                    
        for land in lands:
            i,j = land
            if (i,j) not in visited:   
                queue = deque([[i,j]])
                area = 0
                visited[(i,j)]  = True 
                while queue:
                    oi,oj = queue.popleft()                                     
                    area += 1
                    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                        new_i,new_j = oi +di ,oj + dj
                        if 0 <=new_i< m and 0<= new_j < n and grid[new_i][new_j] == 1 and (new_i,new_j) not in visited:
                            queue.append([new_i,new_j])
                            visited[(new_i,new_j)] = True                    
                max_area = max(max_area,area)     
        
        return max_area
``` 



## 思路 dfs
``` python
class Solution(object):
    def maxAreaOfIsland_dfs(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) + area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0]))
``` 













