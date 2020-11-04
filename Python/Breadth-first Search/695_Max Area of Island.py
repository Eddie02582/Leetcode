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
        
    def maxAreaOfIsland_dfs(self, grid):
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) + area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
      


      
sol = Solution()
sol.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
