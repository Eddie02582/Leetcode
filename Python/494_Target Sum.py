class Solution(object):        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if total < S or (total + S) % 2 == 1:
            return 0    
     
        n = len(nums)
        target = (total + S)//2        
        dp = [ [1 if  j== 0 else 0 for j in range(target + 1)] for i in range(n + 1)] 
      
        for i in range(1,n + 1):
            for j in range(target + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]];
                else:
                    dp[i][j] = dp[i-1][j];
    
        return dp[n][target]                 
        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if total < S or (total + S) % 2 == 1:
            return 0    
     
        n = len(nums)
        target = (total + S)//2        
        dp = [0] * (target + 1)
        dp[0] = 1
      
        for i in range(1,n + 1):
            for j in range(target + 1,-1,-1):
                if j >= nums[i - 1]:
                    dp[j] = dp[j] + dp[j-nums[i-1]]
                else:
                    dp[j] = dp[j];
    
        return dp[target]             
        
sol = Solution()
sol.findTargetSumWays([1, 1, 1, 1, 1],3)


