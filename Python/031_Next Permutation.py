'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
       
        def reverse(nums,start):
            i ,j= start,len(nums) - 1
            while i < j:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        p = len(nums) - 2       
        
        while p >= 0 and nums[p + 1] <= nums[p]:         
            p -= 1  
           
        if p >= 0:
            q = len(nums) - 1
            while q >= 0 and nums[q] <= nums[p]:
                q -= 1
            
            nums[q],nums[p] = nums[p], nums[q]

        #nums = nums[0:p + 1] +nums[p + 1:][::-1]
        reverse(nums,p + 1)
        print (nums)











