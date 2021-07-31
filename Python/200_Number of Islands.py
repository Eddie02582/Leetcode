class Solution:
    def numIslands_dfs(self, grid: List[List[str]]) -> int:

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

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        m,n = len(grid),len(grid[0])
        num_island = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":                   
                    queue = deque([(i,j)])
                    grid[i][j] == "*"
                    while queue:
                        x,y = queue.popleft()                        
                        for r,c in [(x + 1,y),(x - 1,y),(x,y - 1),(x, y+ 1)]:
                            if 0 <= r < m and 0<= c <n and grid[r][c] == "1":  
                                queue.append((r,c))
                                grid[r][c] = "*"                                      
                    num_island += 1        
        return num_island


sol = Solution()


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

sol.numIslands(grid)





sol.numIslands([["1","0","1","1","0","1","1"]])

        
        
        
        
        
    