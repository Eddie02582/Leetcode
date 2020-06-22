class Solution(object):
    def uniquePaths_by_math(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # (m + n - 2)! /((m - 1) ! * (n - 1))
        def factorial(n):
            if n == 1:
                return n
            else:
                return n * factorial(n-1)
        
        if m == 1 or n == 1:
            return 1       
                
        return factorial(m + n - 2)//(factorial(m -1) * factorial(n - 1))
        

    def uniquePaths_dp(self, m: int, n: int) -> int: 
        table = [[0] * m for _ in range(n)]   
        table[0][0] = 1
        
        for i in range(n):
            for j in range(m):        
                if i == 0 or j == 0:              
                    table[i][j] = 1
                else:                 
                    table[i][j] = table[i - 1][j] +table[i][j - 1]    
        return table[n - 1][m - 1] 


    def uniquePaths_res_dp(self, m, n):
        visited = dict()
        def check_path(m,n,visited):            
            if (m, n) in visited:
                return visited[(m, n)]  

            if m == 1 or n == 1:
                return 1                
            result = check_path(m - 1, n ,visited) + check_path(m, n - 1,visited)
            visited[(m, n)] = result           
            return result

        return check_path(m,n,visited)
        









sol = Solution()

print (sol.uniquePaths_dp(7,3))