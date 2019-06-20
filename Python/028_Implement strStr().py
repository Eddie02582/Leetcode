'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

'''

class Solution(object):
    def strStr(self, haystack, needle):
        length=len(needle)
        for i in range(0,len(haystack)-length+1):
            if haystack[i:i+length]==needle:                
                return i            
        return -1      
    
    
sol =Solution()

assert sol.strStr('hello','ll')==2

assert sol.strStr('aaaaa','bba')==-1

assert sol.strStr('','')==0