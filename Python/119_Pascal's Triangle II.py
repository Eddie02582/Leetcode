class Solution:
    def getRow_by_last(self, rowIndex):      
        res = []
        for i in range (0,rowIndex+1):
            row = [] 
            for j in range (i + 1):
                if j == 0 or j == i : 
                    row.append(1)
                else:
                    row.append( res[i - 1][j - 1] + res[i - 1][j])
            res.append(row)
        return res[-1]


#  [k][0] :1
#  [k][1] :1 * k
#  [k][2] :1 * k * ( k - 1) / 2
#  [k][3] :[1 * k * ( k - 1) / 2 ] * ( k - 2 ) / 3


    def getRow(self, rowIndex):      
        res = []
        
        for i in range (rowIndex + 1):
            if i == 0 or i == rowIndex:
                res.append(1)
            else:
                res.append( res[-1] * ( rowIndex - i + 1) // i)
        return res

      
      
      
sol = Solution()

ans = [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

assert sol.getRow(3) == [1,3,3,1]