'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

class Solution(object):
    def rotate_slice(self, nums, k):
        k = k % len(nums)
        array  = nums[len(nums)-k:] + nums[:len(nums)-k]
        for i in range(len(array)):
            nums[i] = array[i]

        
    def rotate_pop(self,nums, k):
        for _ in range(k):
            tmp = nums.pop()
            nums.insert(0, tmp)    

    #timeout    
    def rotate_move(self, nums, k):
        for i in range(0,k):
            temp = nums[-1]
            for j in range(len(nums)- 1 ,-1,-1):                
                nums [j] = nums [j - 1]        
            nums [0] = temp         
        return nums

      
        
sol = Solution()
print (sol.rotate([1,2,3,4,5,6,7],3))          
            
            

 