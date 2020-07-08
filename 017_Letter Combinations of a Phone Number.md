# Letter Combinations of a Phone Number


## 原題目:
```
Given a string containing digits from 2-9 inclusive, return all
 possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.

 dict ={
     '2':['a','b','c'],
     '3':['d','e','f'],
     '4':['g','h','i'],
     '5':['j','k','l'],
     '6':['m','n','o'],
     '7':['p','q','r','s'],
     '8':['t','u','v'], 
     '9':['w','x','y','z'],  
 }       


Example:

    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

## 思路1
使用遞迴每次拆一個digit,並把剩下的digit傳入


## Code

#### Python

```python
        if not digits:
            return []
        
        phone = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}  
        
        res = []
        
        def backtracking(res_digital,s):
            if not res_digital:
                res.append(s)
                return   
            for letter in phone[res_digital[0]]:
                backtracking(res_digital[1:],s + letter )
        
        
        backtracking(digits,'')
        return res
```

## 思路2

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}  
        
        res = []
        def backtracking(start,s):
            if len(s) == len(digits):
                res.append(s)
                return
            
            for i in range(start,len(digits)):
                digit = digits[i]
                for letter in phone[digit]:
                    backtracking(i + 1,s + letter )
        
        
        backtracking(0,'')
        return res
```        




