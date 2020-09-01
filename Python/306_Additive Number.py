class Solution:        
    def isAdditiveNumber(self, num):
        
      
        def backtracking(start,sol):          
            if len(sol) >= 3:
                if sol[-1] != sol[-2] + sol[-3]:
                    return False
                if start == len(num):                  
                    return True            


            for i in range(start,len(num)): 
                s = num[start : i + 1]
                if len(s) > 1 and s[0] == '0':
                    return False
                if backtracking(i + 1,sol + [int(s)] )== True:
                    return True
            return False  

        if len(num) < 3:
            return False
        return backtracking(0,[])      
        
sol = Solution()
sol.isAdditiveNumber("112358")
sol.isAdditiveNumber("199100199")
sol.isAdditiveNumber("1023")