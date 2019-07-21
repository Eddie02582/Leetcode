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
            print (k,t)
            first,last  = 0,0
            if k > t:
                first,last = index+t,index+k
            elif k<= t :
                last,first = index+k,index+t
            if first ==index:
                index -= 1
            
            if n in nums[index+1:first]:
                firstindex = nums[index:first].index(n)
                if n in nums[firstindex+1:last]:
                    return True                
  
        return False    
