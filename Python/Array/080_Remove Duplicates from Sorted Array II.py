'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

    Given nums = [1,1,1,2,2,3],

    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

    It doesn't matter what you leave beyond the returned length.

    Example 2:

    Given nums = [0,0,1,1,1,1,2,3,3],

    Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

    It doesn't matter what values are set beyond the returned length.
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0        
        
        p ,count = 0,0
        for n in nums:       
            if nums[p] != n:
                count = 1
                p += 1
                nums[p] = n
            elif count == 0:                
                count += 1               
            elif count < 2:                 
                p += 1
                count += 1                    
                nums[p] = n         
        
        return p + 1
        
    def removeDuplicates_pointer(self, nums):          
        
        p ,count = -1,0
        for n in nums:       
            if nums[p] != n:
                count = 1
                p += 1
                nums[p] = n
            elif count == 0:
                p += 1
                count += 1               
            elif count < 2:                 
                p += 1
                count += 1                    
                nums[p] = n         
        
        return p + 1        
        
       
        
sol =Solution()

assert sol.removeDuplicates([1,1,1,2,2,3]) == 5

assert sol.removeDuplicates([0,0,1,1,1,1,2,3,3]) == 7

assert sol.removeDuplicates([]) == 0

assert sol.removeDuplicates([1]) == 1













