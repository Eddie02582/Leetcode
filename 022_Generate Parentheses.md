# Generate Parentheses

## 原題目:
```
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## 思路
dfs/backtracking問題,判斷條件,當left或right大於n時,或right 大於left,當left ==n 和 right ==n時即為答案(left 大於right前面以判斷)

## Code

#### Python

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtracking(left,right,s):
            if left > n or right > n or right > left:
                return            
            if left == n and right == n:
                res.append(s)
                return
           
            backtracking(left + 1,right,s + "(")           
            backtracking(left ,right + 1 ,s + ")")
        
        backtracking(0,0,'')
        
        return res
        
```







