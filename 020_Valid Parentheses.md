# Valid Parentheses


## 原題目:
```
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
```

## 思路1
建立配對的字典,利用堆疊概念,迴圈每個字元,進來的是左括號的話,就把它存入stack陣列,為右括號把陣列最上層移出判斷是否配對成功,最後判斷陣列是否全配對完成

## Code

#### Python

```python
class Solution:
    def isValid(self, s):
        result=[]
        dict={')':'(','}':'{',']':'['}
        for x in s:
            if not result or x not in dict:
                result.append(x)
            elif dict[x] != result.pop():
                return False
        
        return result==[]

    def isValid__(self, s): 
        match = {")":"(","}":"{","]":"["}
        stack = []
        for p in s:
            if p not in match:
                stack.append(p)
            elif not stack or stack.pop() != match[p]:
                return False

        return not stack
```







