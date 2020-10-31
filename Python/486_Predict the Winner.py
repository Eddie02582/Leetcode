class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        m = len(nums)
        dp = [[[0,0]] * m  for _ in range(m)]
       
        for i in range(m):
            dp[i][i] = [nums[i],0]
            
        
        for i in range(m - 1,-1,-1):
            for j in range(i + 1,m):
                choose1 = [dp[j][j][0] + dp[i][j - 1][1],dp[j][j][1] + dp[i][j - 1][0]]  
                choose2 = [dp[i][i][0] + dp[i + 1][j][1],dp[i][i][1] + dp[i + 1][j][0]]   
                dp[i][j] = max(choose1 ,choose2)
        
        
        return dp[0][m - 1][0] >=dp[0][m - 1][1]