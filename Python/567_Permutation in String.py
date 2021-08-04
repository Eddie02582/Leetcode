class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        count,window = {},{}
        for s in s1:
            count[s] = count.get(s,0) + 1
       
        l,r = 0,0  
        while r < len(s2):
            if s2[r] in count:
                window[s2[r]] = window.get(s2[r] ,0) + 1    
            if r >= len(s1):
                if s2[l] in count:
                    window[s2[l]] = window.get(s2[l] ,0) - 1    
                l += 1
            if window == count:
                return True
            r += 1              
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter, defaultdict
        match = Counter(s1)
        window = defaultdict(int)
        l,r = 0,0

        while r < len(s2):

            if s2[r] in match:
                window[s2[r]] += 1

            if r - l + 1 == len(s1):     
                if window == match:
                    return True
                elif s2[l] in window:
                    window[s2[l]] -= 1
                l += 1       
            r += 1        
        return False
        
sol = Solution()
assert sol.checkInclusion("ab","eidbaooo") == True
assert sol.checkInclusion("ab","eidboaoo") == False
assert sol.checkInclusion("ab","ab") == True
assert  sol.checkInclusion("abcdxabcde","abcdeabcdx") == True
