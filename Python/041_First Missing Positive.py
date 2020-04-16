class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(n):
            while nums[i] > 0 and  nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index],nums[i]            
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1;
        
        return len(nums) + 1

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums) + 1):
            if i not in nums:
                return i
        
        return len(nums) + 1   
        
        
        
sol = Solution()

assert sol.firstMissingPositive([1,2,0]) == 3

assert sol.firstMissingPositive([3,4,-1,1]) == 2

assert sol.firstMissingPositive([7,8,9,11,12]) == 1

assert sol.firstMissingPositive([2147483647]) == 1