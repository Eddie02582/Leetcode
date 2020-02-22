# Length of Last Word

## 原題目:
```
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

    Input: "Hello World"
    Output: 5
```

## 思路
這邊要注意如果字串全空白或是字串為空切割會有問題


#### Python

``` python
class Solution(object):
    def lengthOfLastWord(self, s):
        if s.rstrip() == '':
            return 0        
        return len(s.split()[-1])
``` 

``` python
class Solution(object):
    def lengthOfLastWord(self, s):      
        array = s.split()
        if not array:
            return 0
        else:
            return len(array[-1]) 
``` 





