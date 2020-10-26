class Solution:
    def numIslands_dfs(self, grid):
        if not grid or not grid[0]:
            return 0
        
        islands = 0     
       
        rows, cols = len(grid), len(grid[0])
        visit = [ [False] * cols for _ in range(rows)]

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == "0" or visit[r][c] :
                return
            
           
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            visit[r][c] = True
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visit[r][c]:
                    islands += 1
                    dfs(r, c)
        return islands

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

        
        
        
        
        
    