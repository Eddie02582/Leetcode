class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l ,r,match = 0,0,0   
        need,window = {},{}
        ans = ""
        for st in t:
            need[st] = need.get(st,0) + 1  
        
  
       
            
        while  r < len(s):
            if s[r] in t:
                window[s[r]] = window.get(s[r],0) + 1
                if window[s[r]] == need[s[r]]:
                    match += 1
                
            while match == len(need):  
                if r - l + 1 < len(ans) or not ans:
                    ans = s[l : r + 1]                
                if s[l] in t:
                    window[s[l]] -= 1
                    if window[s[l]] < need[s[l]]:
                        match -= 1
                l += 1    
            r += 1
        return ans
                
        
            
                
sol = Solution()
sol.minWindow("ADOBECODEBANC","ABC")