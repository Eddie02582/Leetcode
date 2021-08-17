# Combinations

## 原題目:
```
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    
Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.
    
Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.
     

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
```



## 思路Sliding Window
雙指針l,r移動
1.移動r,直到符合所需的字元,
2.移動l,並且記錄最短的字串,直到包含不符合


#### Python
``` python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter,defaultdict        
        window = defaultdict(int)
        need = Counter(t)
        l,r,match = 0,0,0 
        result = ""
        
        
        while r < len(s):  
            
            if s[r] in need:                
                window[s[r]] += 1   
                if window[s[r]] == need[s[r]]:
                    match += 1              
                   
            while match == len(need):                  
                result = s[l:r+ 1] if not result else min(result,s[l:r+ 1],key = len)    
                
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < need[s[l]]:
                        match -= 1
                l += 1   
             
            r += 1 
        return result
```








