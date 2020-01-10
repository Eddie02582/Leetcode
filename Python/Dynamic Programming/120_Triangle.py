class Solution(object):
    def minimumTotal_divide_without_hashmap(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """        

        def dfs (x,y,triangle):
            n = len(triangle)
            print (x,y)
            if x == n:               
                return 0
            return min(dfs(x + 1, y, triangle), dfs(x + 1, y + 1, triangle) + triangle[x][y])
     
        if not triangle:
            return -1
        
       
        result = dfs (0,0,triangle)
        return result
           
    
    def minimumTotal_divide_hashmap(self, triangle):        
        def dfs (x,y,triangle,hashmap):
            n = len(triangle)
            if x == n:               
                return 0
            if hashmap[x][y] != -2**31 + 1:                
                return hashmap[x][y]

            x1y = dfs (x + 1,y,triangle,hashmap)
            x1y1 = dfs (x + 1,y + 1,triangle,hashmap)
            hashmap[x][y] = min(x1y,x1y1) + triangle[x][y]

            return hashmap[x][y]

         
        if not triangle:
            return -1
      
        hashmap = [[ -2**31 + 1 for j in range(len(triangle[i]))]    for i in range(len(triangle))]

        result = dfs (0,0,triangle,hashmap)
        return result   
 
        
    def minimumTotal_dynamic_top(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
       
        n = len(triangle)
        
        for row in range(1,n):
            m = len(triangle[row])
            for col in range(m):
                if col == 0:
                    triangle[row][col] += triangle[row-1][col]
                elif col == m-1:
                    triangle[row][col] += triangle[row-1][col-1]
                else:
                    triangle[row][col] += min(triangle[row-1][col-1],triangle[row-1][col])
        
        return min(triangle[n-1])           
        
        
        
        
        
        
        
        
    
    
sol = Solution() 
array = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

assert sol.minimumTotal_dynamic_top(array) == 11


assert sol.minimumTotal_dynamic_top([[-10]]) == -10