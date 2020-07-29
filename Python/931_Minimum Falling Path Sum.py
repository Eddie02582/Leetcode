class Solution:
    def minFallingPathSum(self, A):
        m = len(A)
        n = len(A[0])
        for i in range(1,m):
            for j in range(0,n):
                if j == 0:
                    A[i][j] = A[i][j] + min(A[i-1][j],A[i-1][j + 1])
                elif j == n - 1:
                    A[i][j] = A[i][j] + min(A[i-1][j - 1],A[i-1][j])
                else:                    
                    A[i][j] = A[i][j] + min(A[i-1][j - 1],A[i-1][j],A[i-1][j + 1])
        print (A)
        return min(A[m - 1])
        
    
    
    
    
    
    
    
    
    
    

A = [
    [1]   
]



sol = Solution()
A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
sol.minFallingPathSum(A)
A = [
    [1]   
]
sol.minFallingPathSum(A)

A = [[51,24],[-50,82]]
sol.minFallingPathSum(A)




#dp[i][j] = A[i][j] + min(A[i-1][:j + 1])