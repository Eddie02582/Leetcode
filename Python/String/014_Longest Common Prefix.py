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
        if strs==[]:
            return "" 
        
        #排序 比較頭尾即可,頭尾差異最大         
        strs.sort()
        min_length=min(len(strs[0]),len(strs[-1]))   
        p = 0 
        while p< min_length:
            if strs[0][p] != strs[-1][p]:
                break 
            p+=1
        return strs[-1][:p]         
        
        
    def longestCommonPrefix(self, strs):
        if strs==[]:
            return ""  
            
        strs.sort()        
        msg = ''
        for x,y in zip(strs[0],strs[-1]):
            if x==y:
                msg += x
            else:
                break
        return msg
                

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