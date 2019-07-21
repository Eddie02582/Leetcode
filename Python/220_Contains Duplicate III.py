'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
    
        for index,n in enumerate(nums):            
            array = nums[index + 1:index + k + 1]
            for p in array:
                if abs(n - p) <= t :
                    return True            
        return False

sol =Solution()  
assert sol.containsNearbyAlmostDuplicate([1,2,3,1],3,0) == True
  
assert sol.containsNearbyAlmostDuplicate([1,0,1,1],1,2) == True

assert sol.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3) == False 

assert sol.containsNearbyAlmostDuplicate([2,1],1,1) == True