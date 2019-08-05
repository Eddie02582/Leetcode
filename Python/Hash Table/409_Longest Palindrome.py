class Solution(object):
    def longestPalindrome(self, s):
        count = {}
        for p in s:
            count [p] = count.setdefault(p,0) + 1
        
        length = 0
        for key in count:
            value = count [key]//2
            length += value *2            
        
        if length < len(s):
            length += 1
        return  length
            