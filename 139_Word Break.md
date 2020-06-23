# Word Break


## 原題目:
```
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                 Note that you are allowed to reuse a dictionary word.

Example 3:

    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: false
```


## 思路
Backtracking,用一個指針計錄目前比對的位置,當取得値不匹配就回溯





## Code



``` python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def backtracking(start,res):
            if s == res:               
                return True            
            
            for word in wordDict:     
                length = len(word)           
                if s[start : start + length + 1] == word:
                    if backtracking(start + len(word),res + word):
                        return True
            
            return  False
        return backtracking(0,"")        
```  


## 思路
DP

``` python
    def wordBreak(self, s,wordDict):       
        length = len(s)
        dp = [False for _ in range(length + 1)]
        dp[0] = True

        for i in range(1, length + 1):
            for j  in range(i):
                word = s[j:i]
                if dp[j] and word in wordDict:              
                    dp[i] = True

        return dp[-1]

```  









