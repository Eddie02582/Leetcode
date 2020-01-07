class Solution(object):
    def firstMissingPositive__(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        
        if not nums:
            return 1
        
        set_nums = set()
        max_number = nums[0]
        for n in nums:
            if n > max_number:
                max_number = n
            
            set_nums.add(n)   
        
        if max_number <0:
            return 1        
        p = 1
        while p < max_number:
            if p not in set_nums:
                return p
            p += 1      
        return max_number + 1
        
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        i = 1
        while True:
            if(i not in nums):
                return i
            i += 1
        
   
        
        
        
sol = Solution()

assert sol.firstMissingPositive([1,2,0]) == 3

assert sol.firstMissingPositive([3,4,-1,1]) == 2

assert sol.firstMissingPositive([7,8,9,11,12]) == 1

assert sol.firstMissingPositive([2147483647]) == 1