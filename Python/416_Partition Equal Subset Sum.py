class Solution(object):        
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)        
        if total % 2 == 1:
            return False
        
        target = total // 2 
        
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1,len(nums)):
            for j in range(target,-1,-1):
                if j >= nums[i - 1]:
                    dp[j] = dp[j] + dp[j-nums[i-1]]
                else:
                    dp[j] = dp[j];                
                if dp[target] > 0:
                    return True
        return dp[-1] > 0 
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)        
        if total % 2 == 1:
            return False
        
        target = total // 2 
        
        dp = [0] * (target + 1)
        dp[0] = True
        for n in nums:
            for i in range(target,n - 1,-1):
                
                dp[i] = dp[i] or dp[i - n]
        return dp[target]

        
sol = Solution()
assert sol.canPartition([1, 5, 11, 5]) == True
assert sol.canPartition([1, 2, 3, 5]) == False

