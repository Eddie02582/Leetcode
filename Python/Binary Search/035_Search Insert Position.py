'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


class Solution(object):
    def searchInsert_(self, nums, target):        
        for i in range(0,len(nums)):
            if target <= nums[i]:               
                return i  
        return len(nums)
        
    def searchInsert(self, nums,target):
        l,r = -1,len(nums)             
       
        while l + 1 < r:
            mid = l + (r - l)//2
            if nums[mid] < target:
                l = mid
            else: 
                r = mid           
        
        return l + 1
        
    def searchInsert(self, nums,target):
        l,r = 0 ,len(nums) - 1             
       
        while l <=  r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: 
                r = mid - 1
            else:
                l = mid + 1
        
        return l        
        
        
    
sol =Solution()

assert sol.searchInsert([1,3,5,6], 5)==2

assert sol.searchInsert([1,3,5,6], 2)==1

assert sol.searchInsert([1,3,5,6], 7)==4

assert sol.searchInsert([1,3,5,6], 0)==0

assert sol.searchInsert([1,3], 2)== 1











