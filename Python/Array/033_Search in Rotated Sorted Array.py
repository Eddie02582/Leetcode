'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    
Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
'''


class Solution(object):
    def search_normal(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            
        return -1
        
    def search(self,nums,target):
        #find piviot index
        if len(nums) == 0:
            return -1

        length = len (nums) 
        l , r  = 0 , length - 1   
      

        while l != r:
            mid = l  + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid


        start = l
        if nums[start] <= target <= nums[length - 1]:
            l , r = start , length - 1
        else:
            l ,r = 0 ,start - 1

        while l <= r:
            mid = l + (r - l ) // 2 
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
  
sol = Solution()       

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]  
print (sol.search(arr,3))

arr = [4, 5,6, 7, 0, 1, 2]  
print (sol.search(arr,0))

arr = [4,5, 6, 7, 0, 1, 2]  
print (sol.search(arr,3))
        
        
arr = [1]  
print (sol.search(arr,1))
        

arr = [1,3]  
print (sol.search(arr,3))