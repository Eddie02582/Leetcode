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


## Dynamic Programming

1.定義狀態
<ul>
	<li>dp[i] 表示 s 的前 i 個字元（即 s[0:i]）是否可以由 wordDict 中的單字組成。</li>
	<li>dp[0] = true，表示空字串是可拆分的（預設成立）</li>
</ul>

計算 dp[1] 到 dp[8] 是否可以由 wordDict 組成：
```
dp[0]  dp[1]  dp[2]  dp[3]  dp[4]  dp[5]  dp[6]  dp[7]  dp[8]
 T      ?      ?      ?      ?      ?      ?      ?      ?
```


2. 狀態轉移方程
對於 dp[i]，我們需要找出一個 j（0 ≤ j < i），使得：

dp[j] == true，即 s[0:j] 可以被拆分成字典中的單字
s[j:i] 在 wordDict 中，即 s[j:i] 這個子字串是一個有效單字

dp[i]=dp[j] 且 s[j:i] 在 wordDict
一旦找到這樣的 j，我們就可以確定 dp[i] = true，否則 dp[i] 仍為 false。

```c++
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());  
        int n = s.size();
        vector<bool> dp(n + 1, false);  
        dp[0] = true; 

        for (int i = 1; i <= n; ++i) {  
            for (int j = 0; j < i; ++j) {  
                if (dp[j] && wordSet.count(s.substr(j, i - j))) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n]; 
    }

   
};
```

優化 j 的遍歷範圍<br>
計算 wordDict 裡最長的單字 maxLen，然後 j 只需要從 max(0, i - maxLen) 開始，減少不必要的遍歷<br>



``` c++
class Solution {
public:
bool wordBreak(string s, vector<string>& wordDict) {
    unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
    int n = s.size(), maxLen = 0;

    for (const string& word : wordDict) {
        maxLen = max(maxLen, (int)word.size());
    }

    vector<bool> dp(n + 1, false);
    dp[0] = true;

    for (int i = 1; i <= n; ++i) {
        for (int j = max(0, i - maxLen); j < i; ++j) {
            if (dp[j] && wordSet.count(s.substr(j, i - j))) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[n];
}


   
};

```  









