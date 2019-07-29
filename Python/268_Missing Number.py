'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

    Input: [3,0,1]
    Output: 2
Example 2:

    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8
'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i,n in enumerate(nums):
            if i !=n:
                return i
        return len(nums)
    #timeout    
    def missingNumber_in(self, nums):        
        for i in range(len(nums)):
            if i not in nums:
                return i
         return len(nums)
         
    def missingNumber_set_in(self, nums):  
        num_set = set(nums)
        for i in range(len(nums)):
            if i not in num_set:
                return i        
        return len(nums)  
          
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = [ i for i in range(len(nums))]
        n = list(set(a)-set(nums) &set(a) )
        
        
        return n[0] if n else len(nums)
        
        
        
        
        
        
        
        