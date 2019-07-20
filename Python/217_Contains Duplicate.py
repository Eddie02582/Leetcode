'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic_count = {}
        for n in nums:
            if n in dic_count:
                return True
            dic_count [n] = 1
        return False
    #timeout
    def containsDuplicate_list(self, nums):   
        array = []
        for n in nums:
            if n in array:
                return True            
            array.append(n)
        return False
    #99.58%
    def containsDuplicate(self, nums):         
        return len(nums) != len(set(nums))  

    def containsDuplicate_set(self, nums):         
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False 










        