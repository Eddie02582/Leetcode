# Remove Duplicate Letters


## 原題目:
```
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
```

<a href = "https://github.com/Eddie02582/Leetcode/blob/master/442_Find%20All%20Duplicates%20in%20an%20Array.md">402	Remove K Digits</a> 的變型


## 思路
要判斷是否有重複可使用set

#### Python

``` python
class Solution(object):        
        ans = 0
        S = list(map(set, words))
        for i in range(len(words)):
            for j in range(i):
                if not S[i] & S[j]: # O(26 * 26) = O(1)
                    ans = max(ans, len(words[i] * len(words[j])))
        return ans
``` 

## 思路
<ul> 
    <li>建立一個字典。其中 key 為 字符 c，value 為其出現的剩餘次數。</li>
    <li>從左往右遍歷字符串，每次遍歷到一個字符，其剩餘出現次數 - 1.</li>
    <li>對於每一個字符，如果其對應的剩餘出現次數大於 1，我們可以選擇丟棄（也可以選擇不丟棄），否則不可以丟棄。</li>
    <li>是否丟棄的標準和上面題目類似。如果棧中相鄰的元素字典序更大，那麼我們選擇丟棄相鄰的棧中的元素。</li>
</ul> 
#### Python


``` python
class Solution:
    def removeDuplicateLetters(self, s) -> int:
        import collections
        stack = []
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and  remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)
``` 

``` python
class Solution:
    def removeDuplicateLetters(self, s) -> int:
        stack = []
        remain_counter = collections.Counter(s)

        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and  remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)
``` 















