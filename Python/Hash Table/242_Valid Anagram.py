'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''

class Solution:     
    def isAnagram_counter(self, s, t): 
        from collections import Counter          
        return Counter(s) == Counter(t)            
                
    def isAnagram_sorted(self, s, t):       
        return sorted(list(s)) == sorted(list(t))     

    def isAnagram_count(self, s, t):
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        for x in set(s):
            if s.count(x) != t.count(x):
                return False
        return True
    
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False    
        array = [ 0 for i in range(26)]
        for p,q in zip(s,t):
            array[ord(p)-97] += 1
            array[ord(q)-97] -= 1 
        
        return all( x==0 for x in array)
    
    
sol =Solution()

s = "anagram"
t = "nagaram"
assert sol.isAnagram(s,t)==True

s = "rat"
t = "car"
assert sol.isAnagram(s,t)==False



