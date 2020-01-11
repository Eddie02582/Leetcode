class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        for row in range(rows):
            for col in range(cols):            
                if grid[row][col] == 0:
                    continue
                total +=4                
                if row - 1 >=0 and grid[row - 1][col]:
                    total -=1
                if row + 1 < rows and grid[row + 1][col]:
                    total -= 1
                if col - 1 >=0 and grid[row][col - 1]:
                    total -= 1        
                if col + 1 < cols and grid[row][col + 1]:
                    total -= 1 
            
        return total
 
    def islandPerimeter(self, grid):
        if not grid:
            return 0        
        ans = 0
        ref = [0]*len(grid[0])
        for lst in grid:
            pre = 0
            for x in range(len(lst)):
                if lst[x] == 1:
                    ans += 4
                    if pre == 1:
                        ans -= 2
                    if ref[x] == 1:
                        ans -= 2
                pre = lst[x]   
            ref = lst
                
        return ans 
     
 
 
sol = Solution()

array = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
         
sol.islandPerimeter(array)





