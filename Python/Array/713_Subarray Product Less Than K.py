class Solution(object):
    def numSubarrayProductLessThanK_(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
      
        count = 0
        for i in range(len(nums)): 
            total = 1
            for j in range(i,len(nums)):                
                total *= nums[j]
                if total < k:
                    count += 1
                else:
                    break    
        return count 
    
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
      
        count ,product ,l = 0,1,0
        for r in range(len(nums)): 
            product *= nums[r]
            while product >= k:
                product //= nums[l];
                l += 1
            count += r - l + 1;  
        return count 
       
    
    
    
    
    
sol = Solution()
nums = [10, 5, 2, 6]
k = 100
sol.numSubarrayProductLessThanK(nums,k)

#[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
















