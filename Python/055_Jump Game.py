class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False    
        
        max_loc = 0        
        for i in range(len(nums)):
            if i > max_loc:
                return False
            if max_loc > len(nums):
                return True            
            max_loc = max(max_loc,nums[i] + i)
        return True