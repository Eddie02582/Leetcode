class Solution:
    def findMin(self, nums):
        if not nums:
            return None
        
        l,r = 0,len(nums) - 1
        
        while l < r:
            mid = (l + r) //2             
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[r]
