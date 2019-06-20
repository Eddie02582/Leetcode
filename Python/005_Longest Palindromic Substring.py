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
        
    def longestPalindrome(self, s):
        if len(s) < 2 or len(set(s))==1:
            return s

        msg,temp=s[0],''
        for i in range (10,len(s)*10-1,5):
            index = i // 10 
            left= index - 1            
            right= index + i % 2        
            temp=self.getPalindrome(s,left,right)

            if len(temp) > len (msg):
                msg=temp  

        return  msg   


    def getPalindrome2(self, s,left,right):  
        
        st=s[left] 
        while left>=0 and  right<len(s) and s[left] == s[right]:   
            st=s[left:right+1]                  
            left, right= left-1 , right+1  
        return st
        
    def getPalindrome(self, s,left,end):  
        
        st=s[left] 
        while left>=0 and  right<len(s) and s[left] == s[right]:   
            st=s[left:right+1]                  
            left, right= left-1 , right+1  
        return st     
        
        
sol =Solution()

assert sol.longestPalindrome("babad")=='bab'

assert sol.longestPalindrome("cbbd")=='bb'

assert sol.longestPalindrome("ac")=='a'

assert sol.longestPalindrome("bb")=='bb'










