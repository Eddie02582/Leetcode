class Solution:
    def findAnagrams(self, s, p):
        if len(s) < len(p):
            return []    
        from collections import Counter
        need = Counter(p)
        window = {}
        match,n = 0,len(p)
        ans = []
        for i in range(len(s)):
            if s[i] in need:
                window[s[i]] = window.get(s[i],0) + 1
                if window[s[i]] == need[s[i]]:
                    match += 1          
            if i >= n:
                if s[i - n] in window:
                    window[s[i - n]] -= 1
                    if window[s[i - n]] < need[s[i - n]]:
                        match -= 1            
            
            if match == len(need):
                ans.append(i + 1 - n)   
        
        return ans
        


sol = Solution()
sol.findAnagrams("cbaebabacd","abc")
sol.findAnagrams("abab","ab")