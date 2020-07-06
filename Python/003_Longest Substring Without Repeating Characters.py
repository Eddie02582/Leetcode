'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
#!/usr/bin/python
# encoding=utf-8
class Solution:  
    '''        
        另用map 紀錄出現字母,right指針向右,如果沒出現就紀錄長度
        ,當出現過的字母,left 指針就跑到重複出現字母的位置 
        
    '''
    def lengthOfLongestSubstring(self, s):    
        left,right,max_length=0,0,0       
        maps = set()
        
        while right < len(s):                
            if s[right] not in maps:
                maps.add(s[right])
                right += 1                 
            else:
                maps.remove(s[left])
                left += 1 
            max_length = max(right-left,max_length)        
        return max_length
        
 

    def lengthOfLongestSubstring_array(self, s):
        locations = [0]*256    
        l,r=0,-1      
        res = 0        
        while l < len(s):                
            if r + 1 < len(s) and not locations[ord(s[r +1])]:  
                r += 1                              
                locations[ord(s[r])] += 1  
               
            else:
                locations[ord(s[l])] -= 1   
                l += 1 
            res =max(res,r - l + 1)
        return res 


    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        position  = [-1] * 256
        res = 0
        l ,r = 0 ,0

        while r < len(s) :  
            index = ord(s[r])   
            if position[index]  >= l:
                l = position[index] + 1 

            res = max(res ,r - l + 1)   
            position[index] = r        
            r += 1   
        return res

    def lengthOfLongestSubstring_map(self, s):
        if not s:
            return 0
        if len(s) <= 1:
            return len(s)
        locations = [-1 for i in range(256)]
        index = -1
        m = 0
        for i, v in enumerate(s):
            if locations[ord(v)] > index:
                index = locations[ord(v)]
            m = max(m, i - index)
            locations[ord(v)] = i
        return m


        
        
   
        
        
        
sol =Solution()


assert sol.lengthOfLongestSubstring('abcabcbb')==3

assert sol.lengthOfLongestSubstring('abcbcbb')==3


assert sol.lengthOfLongestSubstring('bbbbb')==1

assert sol.lengthOfLongestSubstring_map('pwwkew')==3

assert sol.lengthOfLongestSubstring(' ')==1

assert sol.lengthOfLongestSubstring('au')==2

