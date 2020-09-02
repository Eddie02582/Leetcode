class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        ans,count = 1,1
        
        for i in range(1,len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            ans = max(ans,count)
        
        return ans