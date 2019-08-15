'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

'''

class Solution(object):
    def sortColors_bubble_sort(self, nums):
        for i in range(len(nums)):
            bsweep = False
            for j in range(0,len(nums) - 1 - i ):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    if not bsweep:
                        bsweep = True
            if not bsweep:
                return
      
  
    def sortColors_counting_sort(self, nums):
        count=[0,0,0]
        for n in nums:
            count[n] += 1   
        j = 0
        for i in range(len(nums)): 
            while count[j] == 0 :            
                j += 1 
            nums[i] = j
            count[j] -= 1   
 
    def sortColors(self, nums):
        zero = -1
        two
        count=[0,0,0]
        for n in nums:
            count[n] += 1   
        j = 0
        for i in range(len(nums)): 
            while count[j] == 0 :            
                j += 1 
            nums[i] = j
            count[j] -= 1   
  
            
sol = Solution()

sol.sortColors([2,0,2,1,1,0])