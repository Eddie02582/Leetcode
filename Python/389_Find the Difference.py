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
    def findTheDifference_sort(self, s, t):
        s = sorted(list(s))
        t = sorted(list(t))
        for p,q in zip(s,t):
            if p != q :
                return q
        return t[-1]
        
    def findTheDifference(self, s, t):                
        return ''.join(c for c in set(t) if s.count(c) != t.count(c))     
     
     
    def findTheDifference_counter(self, s, t):
        from collections import Counter         
        return next((Counter(t)-Counter(s)).elements())       
  
        
        
    def findTheDifference_remove(self, s, t):         
        t = list(t)
        for p in s:
            t.remove(p)                
        return t[0]            
        
    def findTheDifference(self, s, t):  
    
        dic_count = {} 
        for i,p in enumerate(t):
            dic_count[p] = dic_count.setdefault(p,0) + 1
            if i < len(s):
                dic_count[s[i]] = dic_count.setdefault(s[i],0) - 1
           
        for p in dic_count:
            if dic_count[p] == 1:
                return p        
        return p      
        
        

sol = Solution()

assert sol.findTheDifference("abcd","abcde") =='e'

   
        
        
        
        
        
        