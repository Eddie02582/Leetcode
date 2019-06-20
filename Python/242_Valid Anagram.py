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
        return Counter(s)==Counter(t)            
                
    def isAnagram_sorted(self, s, t):       
        return sorted(list(s)) == sorted(list(t))     

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        for x in set(s):
            if s.count(x) != t.count(x):
                return False
        return True

sol =Solution()

s = "anagram"
t = "nagaram"
assert sol.isAnagram(s,t)==True

s = "rat"
t = "car"
assert sol.isAnagram(s,t)==False



