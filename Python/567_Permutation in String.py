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

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        need,window = {},{}
        
        for s in s1:
            need[s] = need.get(s,0) + 1
          
        l,r,match = 0,0,0        
        while r < len(s2):
        
            if s2[r] in need:
                window[s2[r]] = window.get(s2[r] ,0) + 1 
                if window[s2[r]] == need[s2[r]]:
                    match += 1
            r += 1
            if match == len(need):
                return True
               
            if r >= len(s1):
                if s2[l] in need:
                    if window[s2[l]] == need[s2[l]]:
                        match -= 1
                    window[s2[l]] = window.get(s2[l] ,0) - 1                      
                l += 1
                         
        return False

        
sol = Solution()
assert sol.checkInclusion("ab","eidbaooo") == True
assert sol.checkInclusion("ab","eidboaoo") == False
assert sol.checkInclusion("ab","ab") == True
assert  sol.checkInclusion("abcdxabcde","abcdeabcdx") == True
