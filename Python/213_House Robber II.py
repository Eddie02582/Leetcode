class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        def get_rob(array):            
            rob1,rob2,temp = 0,0,0
            for n in array:
                rob1,rob2 = rob2,max(rob1 + n,rob2 )
            
            return rob2
        
        
        return max(get_rob(nums[0:-1]),get_rob(nums[1:]))    


sol = Solution()
sol.rob([1,2,3,1]))
sol.rob([2,7,9,3,1]))         
sol.rob([2,1,1,2]))   