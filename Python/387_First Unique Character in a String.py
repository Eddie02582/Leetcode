'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

Accepted
'''

class Solution(object):
    #timeout
    def firstUniqChar_count(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i,p in enumerate(s):
            if s.count(p) == 1:
                return i
        return -1
        
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for p in s:
            dict [p] = dict.setdefault(p,0) + 1  
                      
        for i,p in enumerate(s):
            if dict[p] == 1:
                return i
        return -1
   
    def firstUniqChar_counter(self, s):
        from collections import Counter
        dict = Counter(s)
            
        for i,p in enumerate(s):
            if dict[p] == 1:
                return i
        return -1
        

sol = Solution()

assert sol.firstUniqChar("leetcode") == 0

assert sol.getSum("loveleetcode") == 2      
        
        
        
        
        
        