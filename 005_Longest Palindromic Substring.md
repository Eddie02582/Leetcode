# Longest Palindromic Substring


## 原題目:

```
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

```

## 思路
<a href = "https://leetcode.com/submissions/detail/386450266/">sol</a>
迴圏歷遍切開字串判斷字串左右兩邊<br>
```
以"babad"
當指針指向b,有2種可能　Palindrome("","babad") 和 Palindrome("","abdab") +"b"
當指針指向a,有2種可能　Palindrome("b","abad") 和 Palindrome("ba","bdab") +"b"
所以當指針i指向某個元素,需要判斷 字串(i - 1,i)之間和(i - 1,i + 1)之間的回文


```



## Code

#### Python
使用map記錄是否出現
```
class Solution:
    def longestPalindrome(self, s: str) -> str:   
        if not s:
            return ''
        #加入這段可以省去當元素皆一樣
        if len(set(s))==1:
            return s    
        ans,palindrome  = s[0],""
        
        #這邊直接從1開始,因為ans初始値已經包含
        for i in range(1,len(s)):
            #a|bc  a|c
            palindrome = self.getPalindrome(i - 1,i,s)
            if len(palindrome) > len(ans):
                ans = palindrome
                
            palindrome = self.getPalindrome(i - 1,i + 1,s)
            if len(palindrome) > len(ans):
                ans = palindrome    
    
        return ans
    
    
    def getPalindrome(self,left,right,s):   
        if left < 0:
            return ""   
        #用來處理(i - 1,i)和(i - 1,i + 1)差異
        palindrome = s[left + 1:right]   
        while left >=0 and  right <=  len(s) - 1 and s[left] == s[right]:            
            palindrome = s[left] + palindrome + s[right]
            left -= 1
            right += 1
        return palindrome        
```
