class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []     
        res = []
        for i in range (0,numRows):
            row = [] 
            for j in range (i + 1):
                if j == 0 or j == i : 
                    row.append(1)
                else:
                    row.append( res[i - 1][j - 1] + res[i - 1][j])
            res.append(row)
        return res



      
sol = Solution()

ans = [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

assert sol.generate(5) == ans