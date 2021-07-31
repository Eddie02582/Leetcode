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

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        islands = 0     
       
        rows, cols = len(grid), len(grid[0])
        visit = [[False] * cols for _ in range(rows)]

        def bfs(r, c):

            q = [(r,c)]
            while q:
                row,col = q.pop(0)
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    r,c = row + dr,col + dc
                    if 0 <= r < rows and 0 <= c <cols  and grid[r][c] == "1" and not visit[r][c]:
                        visit[r][c] = True
                        q.append((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visit[r][c]:
                    islands += 1
                    bfs(r, c)
        return islands


sol = Solution()


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

sol.numIslands(grid)





sol.numIslands([["1","0","1","1","0","1","1"]])

        
        
        
        
        
    