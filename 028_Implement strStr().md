# Implement strStr()

## 原題目:
```
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

## 思路
用迴圈歷遍整個,再利用while 一一比較字,如果字相同,q會等於needle 的長度

## Code

#### Python

```python
class Solution(object):
    def strStr(self, haystack, needle):        
        length = len(needle)        
        for i in range(len(haystack) - length + 1):
            p ,q = i ,0           
            while q < length :
                if haystack[p] != needle[q]:
                    break
                q += 1
                p +=1
            
            if q == length:
                return i
            
        
        return -1     
```
簡單的寫法
```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        if len(haystack) < length:
            return -1
        
        for i in range(0,len(haystack) - length + 1):
            if haystack[ i: i + length] == needle:
                return i      
        
        return -1
```




