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

class Solution:
    def lengthOfLongestSubstring(self, s):
        left,right,max_length=0,1,0
        if len(s)<2:
            return len(s)
            
        mgs=s[0]
        
        while right<len(s):        
            if s[right] not in mgs:
                mgs+=s[right]
                right+=1
            else:
                max_length=max(right-left,max_length)
                left+=1
                mgs=s[left:right] 
            
            if right==len(s):
                max_length=max(right-left,max_length)
            
        return max_length

    def lengthOfLongestSubstring2(self, s):
        if not s:
            return 0
        if len(s) <= 1:
            return len(s)
        locations = [-1 for i in range(256)]
        index = -1
        m = 0
        for i, v in enumerate(s):
            if (locations[ord(v)] > index):
                index = locations[ord(v)]
            m = max(m, i - index)
            locations[ord(v)] = i
        return m

    '''
        一般的解法 速度較慢
    '''
    def lengthOfLongestSubstring_Normal(self, s):       
        tempstring=""
        result=""	
        for i in range(len(s)):			
            tempstring=s[i]
            for j in range(i+1,len(s)):
                if  s[j] in tempstring:
                    break
                else:
                    tempstring+=s[j]			
            if len(tempstring)> len(result):
                result=tempstring 
        return len(result)
		        
        
        
        
        
sol =Solution()

print (sol.lengthOfLongestSubstring('abcabcbb'))

print (sol.lengthOfLongestSubstring('bbbbb'))

print (sol.lengthOfLongestSubstring('pwwkew'))

print (sol.lengthOfLongestSubstring(" "))

print (sol.lengthOfLongestSubstring("au"))