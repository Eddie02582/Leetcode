class Solution:                
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0  
        
        l,r,total = 0,0,0
        ans = float('inf')

        while l <= r and  r < len(nums):
            total += nums[r]
            while total >= s:
                ans = min(ans,r - l + 1)
                total -= nums[l]
                l += 1  
            r += 1
     
        return  0 if ans == float('inf') else ans



sol = Solution()
sol.minSubArrayLen(7,[2,3,1,2,4,3])

#sol.minSubArrayLen(15,[5,1,3,5,10,7,4,9,2,8])

#sol.minSubArrayLen(11,[1,2,3,4,5])

#sol.minSubArrayLen(6,[10,2,3])

sol.minSubArrayLen(6,[7])