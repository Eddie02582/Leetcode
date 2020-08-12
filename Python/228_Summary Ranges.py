class Solution:
    def summaryRanges_(self, nums):
        if not nums:
            return []
        
        data = [nums[0]]
        ans = []      
        

        for i in range(1,len(nums)):
            if nums[i] - nums[i -1] == 1:
                data.append(nums[i])
            else:
                if len(data) > 1:
                    ans.append("{0}->{1}".format(data[0],data[-1]))
                else:
                    ans.append("%s"%data[0])
                
                data = []
                data.append(nums[i])
        if data:
            if len(data) > 1:
                ans.append("{0}->{1}".format(data[0],data[-1]))
            else:
                ans.append("%s"%data[0])    
        
        return ans
        
    def summaryRanges(self, nums):
        if not nums:
            return []              
        l,r = 0,1            
        ans = []
        while r <= len(nums):
            if r == len(nums) or nums[r] - nums[r - 1] != 1:
                if r - l == 1:
                    ans.append("%s" %nums[l])
                else:
                    ans.append("{0}->{1}".format(nums[l],nums[r - 1]))
                l = r            
            r += 1             
        return ans

sol = Solution()
sol.summaryRanges([0,2,3,4,6,8,9])

#["0","2->4","6","8->9"]