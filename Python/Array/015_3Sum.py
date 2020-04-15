#!/usr/bin/python
# encoding=utf-8
'''

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''

class Solution:
    def threeSum(self, nums):
    
        if len(nums)<3:
            return []
            
        nums.sort() 
        if nums[0] > 0:
            return []
            
        res = []        
        for i in range(len(nums) - 2):             
            if i == 0 or nums[i] != nums[i - 1]:                 
                l,r = i + 1, len(nums) - 1  
                while l < r:
                    total = nums[i] + nums[l] +  nums[r]   
                    if total > 0:
                        r -= 1
                    elif total < 0:
                        l += 1                   
                    else:
                        array = [nums[low],nums[i],nums[high]]                          
                        if array not in res:
                            res.append(array) 
                        r -= 1
                        l += 1    

                    
        return res   

class Solution:    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)< 3:
            return []        
        nums.sort()        
        res = []
        
        for i in range(len(nums) - 2):   
            if i == 0 or nums[i] != nums[i - 1]:  
                l,r = i + 1, len(nums) - 1
                while l < r:
                    total = nums[i] + nums[l] +  nums[r]                    
                    if total > 0:
                        r -= 1
                    elif total < 0:
                        l += 1
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                        r -= 1
                        l += 1
                        while l < r and  nums[l] == nums[l - 1]:                            
                            l += 1                     
                        while l < r and  nums[r] == nums[r + 1]:                            
                            r -= 1          
        return res









        
