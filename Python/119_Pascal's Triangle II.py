class Solution:

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

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """    
        dp = [0] * (rowIndex + 1 )
        dp[0] = 1
        for i in range(1 ,rowIndex + 1):
            for j in range(rowIndex - 1,0,-1):
                dp[j] = dp[j] + dp[j - 1]
            dp[i] = 1
        return dp      
      
      
sol = Solution()

ans = [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

assert sol.getRow(3) == [1,3,3,1]