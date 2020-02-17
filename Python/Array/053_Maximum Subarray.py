'''

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

'''

class Solution(object):

    def maxSubArray_normal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in range(len(nums)):
            temp = 0
            j = i 
            while (temp >= 0 and j < len(nums)):
                temp += nums[j] 
                result = max(result,temp)
                j += 1

        return result
        
    def maxSubArray(self, nums):
   
        temp = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):            
            if temp < 0:
                temp = 0  
            temp += nums[i]             
            result = max(result,temp)  
        return result
        
        
sol =Solution()

assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])==6

assert sol.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4])==6

#2,1,-2,1,4,