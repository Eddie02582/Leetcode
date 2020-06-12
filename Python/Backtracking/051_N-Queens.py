class Solution:
    def solveNQueens(self, n) : 
        m = 2*n - 1
        mx,my,md1,md2 = [False] * n,[False] * n,[False] * m,[False] * m
        sol = [[""]*n for i in range(n)]
        res = []
        def backtracking(x,y,c):
            if y == n:
                x += 1
                y = 0        
            if x == n:
                if c == n:                    
                    res.append( [ ".".join(row) for row in sol])
                return
            
            d1 = (x + y) % m
            d2 = (x - y + m) %m
            
            if not mx[x] and not my[y] and not md1[d1] and not md2[d2]:
                mx[x],my[y],md1[d1],md2[d2] = True,True,True,True
                sol[x][y] = "Q"
                backtracking(x,y + 1,c + 1)
                mx[x],my[y],md1[d1],md2[d2] = False,False,False,False
            
            sol[x][y] = ""
            backtracking(x,y + 1,c)

        backtracking(0,0,0)
        return res

    def solveNQueens_modify(self, n) : 
        m = 2*n - 1
        my,md1,md2 =[False] * n,[False] * m,[False] * m
        sol = [[""]*n for i in range(n)]
        res = []
        def backtracking(x):     
            if x == n: 
                res.append( [ ".".join(row) for row in sol])
                return
            
            for y in range(n):   
                d1 = (x + y) % m
                d2 = (x - y + m) %m            
                if not my[y] and not md1[d1] and not md2[d2]:
                    my[y],md1[d1],md2[d2] = True,True,True
                    sol[x][y] = "Q"
                    backtracking(x + 1)
                    my[y],md1[d1],md2[d2] = False,False,False            
                    sol[x][y] = ""
                

        backtracking(0)
        return res



sol = Solution()
sol.solveNQueens_modify(4)
  
# This code is contributed by Shiv Shankar 