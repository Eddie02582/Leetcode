'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

'''

class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        ans = nums[0]
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i - 1] + nums[i],nums[i])
            
            ans = max(ans,dp[i])
        
        return ans
        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prev = nums[0]     
        ans = nums[0]
        
        for i in range(1,n):
            prev = max(prev+ nums[i],nums[i])            
            ans = max(ans,prev)        
        return ans

        
        
sol =Solution()

assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])==6

assert sol.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4])==6

#2,1,-2,1,4,