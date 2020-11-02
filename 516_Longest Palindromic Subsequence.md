# Longest Palindromic Subsequence


## 原題目:
```
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
 

Example 2:
Input:

"cbbd"
Output:
2
```

## 思路dp

要判斷dp[i][j]是否有回文兩種情況,
s[i] == s[j]
```
    i   j
b b b a b
則dp[i][j]會從dp[i + 1][j - 1] + 2
```
s[i] != s[j]
```
    i   j
b b b a a
則dp[i][j]回文一定是dp[i][j - 1],dp[i + 1][j]最大値
```




#### Python
``` python
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        n = len(s)
        dp = [ [0] * n for _ in range(len(s))]
        
        for i in range(n - 1, -1,-1):
            for j in range(i,n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max (dp[i][j - 1],dp[i + 1][j])       
       
        return dp[0][-1]
                
``` 












