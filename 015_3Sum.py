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


##Time Out
class Solution_TimeOut:    
    def threeSum(self, nums):
        result=[]
        if len(nums)<=3 and sum(nums)==0:
            return nums
       
        for i in range(len(nums)):
            for j in range(i+1,len(nums)-1):
                if -(nums[i]+nums[j]) in nums[j+1:]:
                    array=sorted([nums[i],nums[j],-(nums[i]+nums[j])])
                    if array not in result:
                        result.append(array)
        return result
        


#Time Out 跟上面差在直接用not in result判斷

class Solution_Modify:    
    def threeSum(self, nums):
        nums.sort() 
        result=[]
        if len(nums)<3:
            return []
            
        for i in range(len(nums)-2):  
        
            if i>0 and nums[i] == nums[i-1]:
                continue  
                
            low = i + 1
            high = len(nums) - 1      
            
            while low < high : 
            
                total= nums[high]+nums[low]+nums[i]
                if total == 0:
                    array=[nums[low],nums[i],nums[high]]  
                    if array not in result:
                        result.append(array) 
                    low+=1
                    high-=1               
                
                elif total>0:
                    high-=1
                else :
                    low+=1
                    
        return result
        
        



class Solution:    
    def threeSum(self, nums):
        nums.sort() 
        result=[]
        if len(nums)<3:
            return []
            
        for i in range(len(nums)-2):  
        
            if i>0 and nums[i] == nums[i-1]:
                continue  
                
            low = i + 1
            high = len(nums) - 1      
            
            while low < high : 
            
                total= nums[high]+nums[low]+nums[i]
                
                if total>0:
                    high-=1
                elif total<0:
                    low+=1
                else:
                    array=[nums[low],nums[i],nums[high]]
                    
                    while high - 1 > low and nums[high] == nums[high - 1]:
                        high -= 1
                    while low + 1 < high and nums[low] == nums[low + 1]:
                        low += 1                   
                    result.append(array) 
                    low+=1
                    high-=1
        return result        
