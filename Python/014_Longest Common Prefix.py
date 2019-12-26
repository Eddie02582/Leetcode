#!/usr/bin/python
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

class Solution:        
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        s , p  = "",0
        while p < len(strs[-1]) and p < len(strs[0]):
            if strs[-1][p] != strs[0][p]:
                break
            s += strs[0][p]
            p += 1
        return s       
        
        
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        s  = ""
        for k,v in zip(strs[-1],strs[0]):
            if k != v:
                break
            s += k 
        return s
                

    def longestCommonPrefix(self, strs):
        if strs==[]:
            return ""   
        msg,s="",strs[0]	
        
        for i in range(1,len(s)+1):
            if  all ( s[:i]==p[:i] for p in  strs):
                msg=s[:i]
            else:
                break
        return msg    

    
    
    
    
    
sol =Solution()

assert sol.longestCommonPrefix(["flower","flow","flight"])=='fl'

assert sol.longestCommonPrefix(["dog","racecar","car"])==''

assert sol.longestCommonPrefix(["car","cat","calculate"])=='ca'