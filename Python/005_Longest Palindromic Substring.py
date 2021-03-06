'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:   
        if not s:
            return ''
        if len(set(s))==1:
            return s    
        ans,palindrome  = s[0],""
        
        for i in range(1,len(s)):
            #a|bc  a|c
            palindrome = self.getPalindrome(i - 1,i,s)
            if len(palindrome) > len(ans):
                ans = palindrome
                
            palindrome = self.getPalindrome(i - 1,i + 1,s)
            if len(palindrome) > len(ans):
                ans = palindrome    
    
        return ans
    
    
    def getPalindrome(self,left,right,s):   
        if left < 0:
            return ""    
        palindrome = s[left + 1:right]   
        while left >=0 and  right <=  len(s) - 1 and s[left] == s[right]:            
            palindrome = s[left] + palindrome + s[right]
            left -= 1
            right += 1
        return palindrome        
        
sol =Solution()

assert sol.longestPalindrome("babad")=='bab'

assert sol.longestPalindrome("cbbd")=='bb'

assert sol.longestPalindrome("ac")=='a'

assert sol.longestPalindrome("bb")=='bb'










