# Valid Parentheses


## 原題目:
```
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
```

## 思路1
建立配對的字典,利用堆疊概念,迴圈每個字元,進來的有兩種情況
<ul>
    <li>左括號:存入stack陣列</li>
    <li>右括號:如果陣列為空,表示不可能配對,如果陣列不為空,把陣列最上層移出判斷是否配對成功</li>
</ul>
如果都都配對完,那個stack為空

## Code

#### Python

```python
class Solution:
    def isValid(self, s): 
        match = {")":"(","}":"{","]":"["}
        stack = []
        for p in s:
            if p not in match:
                stack.append(p)
            elif not stack or stack.pop() != match[p]:
                return False

        return not stack
```







