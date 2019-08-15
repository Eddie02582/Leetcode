'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

'''

class Solution(object):
    def maxSubArray(self, nums):
   
        temp = nums[0]
        Max =temp
        
        for i in range(1,len(nums)):
            if temp <0:
                temp=0
            temp +=nums[i]
            if temp > Max:
                Max=temp  
        return Max
        
        
sol =Solution()

assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])==6

assert sol.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4])==6

#2,1,-2,1,4,