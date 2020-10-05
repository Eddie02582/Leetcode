class Solution:
    def lengthOfLIS_(self, nums):
        if not len(nums):
            return 0
        dp = [1] * len(nums)  
        
        for i in range(1,len(nums)): 
            index = i - 1
            while index >= 0:
                if nums[i]  > nums[index] and dp[index] + 1 > dp[i]:
                    dp[i] = dp[index] + 1             
                index -= 1              
        return max(dp)

    def lengthOfLIS(self, nums):
        LIS = []
        for num in nums:
            list_nb = self.binary_search(num,LIS)
            if list_nb  == len(LIS) - 1:
                LIS.append(num)
            else:
                LIS[list_nb + 1] = min(num,LIS[list_nb + 1])
        
        return len(LIS)
    
    def binary_search(self,num,LIS):
        left ,right = 0, len(LIS) - 1
        while left <= right :
            mid = (left + right)//2
            if num <=LIS[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return right
            
        
sol = Solution()
#sol.lengthOfLIS([10,9,2,5,3,7,101,18])
sol.lengthOfLIS([4,10,4,3,8,9])
#sol.lengthOfLIS([1,3,2])
sol.lengthOfLIS([1,3,6,7,9,4,10,5,6])
