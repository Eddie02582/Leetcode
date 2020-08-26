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

類似作法,改成記錄每次digits位置
```python
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {'2':"abc",'3':"def",'4':'ghi','5':'jkl','6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans = []
        def backtracking(word,index):
            if len(word) == len(digits):
                ans.append(word)
                return            
            for letter in mapping[digits[index]]:
                backtracking(word + letter,index + 1)        
        backtracking("",0)   
        return ans
```



## 思路2
使用雙層迴圈第一層歷遍所在digital,第2層對應的文字,意外的比思路1快,是因為減少遞迴次數?

<a href = "https://leetcode.com/submissions/detail/383624541/">Accepted Solutions</a>
```python
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {'2':"abc",'3':"def",'4':'ghi','5':'jkl','6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans = []
        def backtracking(word,start):
            if len(word) == len(digits):
                ans.append(word)
                return
            for i in range(start,len(digits)):
                for letter in mapping[digits[i]]:
                    backtracking(word + letter,i + 1)        
        backtracking("",0)   
        return ans
```        




