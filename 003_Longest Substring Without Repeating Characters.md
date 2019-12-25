# Longest Substring Without Repeating Characters


## 原題目:

```
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

```

## 思路1
利用set 判斷是否出現過,使用雙指針left,right,如果重複將新的left 指針移到第一次出現的位置,並且清空maps <br>

ex: "pwwkew" <br>
1. pww  ->   l = 0 , r = 1 ,s = pw <br>
2. 移動 ->   l = 2 , r = 3 <br>
3. wkew ->   l = 2 , r = 5 , s = wke <br>

## Code

#### Python

```
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left,right,ans = 0,0,0       
        maps = set()
        while right < len(s):
            if s[right] in maps:                
                while s[left] != s[right]:
                    left += 1
                left += 1
                maps.clear()                                          
                right = left                         
            maps.add(s[right])  
            right += 1                     
            ans = max(len(maps),ans)
        return ans
```

## 思路2
簡化思路1,另用map 紀錄出現字母,right指針向右,如果沒出現就紀錄長度,當出現過的字母,left 指針就跑到重複出現字母的位置 <br> 

ex: "pwwkew" <br>
1. pww  ->   l = 0 , r = 2 ,len = 2 ,maps = (p,w)<br>
2. 移動 ->   l = 1 , r = 2 ,maps = (w)<br>
3. 移動 ->   l = 2 , r = 2 ,maps = ()<br>
4. wkew ->   l = 2 , r = 5 ,maps = (wke)<br>

python
```
class Solution: 

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
            max_length=max(right-left,max_length)        
        return max_length
```        

## 思路3
利用array 陣列記錄出現字的位置,index 為起始位置,當重複出現字,更新index位置


```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
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
```





