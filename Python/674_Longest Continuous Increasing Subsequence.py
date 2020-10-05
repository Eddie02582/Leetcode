class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        ans = 1
        for i in range(n):            
            for j in range(i + 1,n):
                if nums[j - 1] >= nums[j]:
                    break
                ans = max(ans,j - i + 1) 
        return ans
    
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0        
        ans,p = 1,0
        
        for i in range(1,len(nums)):   
            if nums[i] > nums[i - 1]:                    
                ans = max(ans,i - p + 1)
            else:
                p = i                
        return ans    
    
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0        
        ans,p = 1,0
        
        for i in range(1,len(nums)):   
            if nums[i] <= nums[i - 1]: 
                p = i
            ans = max(ans,i - p + 1)                  
        return ans  
    
    
    
    
    
    
    
    
    
    
    
    
    
sol = Solution()
assert sol.findLengthOfLCIS([1,3,5,4,7]) == 3