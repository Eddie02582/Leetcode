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

## 思路
雙指針l,r,l記錄字串第一個字的所在位置,r指針移動當s[r]重複,將l指針移到與s[r]値一樣的下一個

1. r 指針移動,記錄長度<br>
2. 判對s[r]是否重複,有更新l位置<br>
3. 記錄長度<br>
4. r = r + 1 <br>

ex: "pwwkew" <br>
1. p ->    l = 0,r = 0 ,string = 'p'
2. w ->    l = 0,r = 1 ,string = 'pw'
3. w 此時重複 -> l需移動到第一次w的下個位置  -> l = 2,r = 2 ,string = 'w'
4. k ->    l = 2,r = 3 ,string = 'wk'
5. e ->    l = 2,r = 4 ,string = 'wke'
6. w ->   此時重複,但r = 5 離開


## Code

#### Python
使用map記錄是否出現
```python
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

利用陣列position記錄字元上次出線的位置
```python
class Solution: 

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
```  

update 20210803

利用字典記錄上次字元出現的位置,如果重複出現將l移動到上次出現的下一個位置

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        loc = {}
        l,r = 0,0
        ans = 0
        while  r < len(s):            
            if s[r] in loc and loc[s[r]] >= l:                
                l = loc[s[r]] + 1                  
                
            ans = max(r - l + 1,ans)    
            loc[s[r]] = r            
            r += 1            
        return ans

```  

















