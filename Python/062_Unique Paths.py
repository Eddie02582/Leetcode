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
                
        return factorial(m + n - 2)/(factorial(m -1) * factorial(n - 1))
        
        
    def uniquePaths(self, m, n):
        r_max = m - 1
        c_max = n - 1
        memo = dict()
        
        def check_path(r=0,c=0):
            
            if r == r_max and c == c_max:
                return 1
            if r > r_max or c > c_max:
                return 0
            # check down and right
            if (r,c) not in memo:
                memo[r,c] = check_path(r + 1,c) + check_path(r, c + 1)
            print (memo[r,c]  )
            return memo[r,c]  

        return check_path()


    def uniquePaths_dp(self, m, n):
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