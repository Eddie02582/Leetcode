'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

'''

class Solution(object):
    def lengthOfLastWord(self, s):
        if s.rstrip() == '':
            return 0        
        return len(s.split()[-1])
        
    def lengthOfLastWord(self, s):      
        array = s.split()
        if not array:
            return 0
        else:
            return len(array[-1])      
        
        
        
        
        
        
    
sol =Solution()

assert sol.lengthOfLastWord("Hello World")==5

assert sol.lengthOfLastWord("a ")==1