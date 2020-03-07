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
使用遞迴每次拆一個digit並與前次結果做雙重迴圈得到下次結果,注意第一次須先產生


## Code

#### Python

```python
class Solution(object):
    def letterCombinations(self, digits):       
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
        
        def helper(array,digits):
            if digits:
                number,digits = digits[0:1],digits[1:]                
                result = []                
                for s in array:
                    for letter in dict[number]:
                        result.append(s + letter)                
                return helper(result,digits)    
            return array
            
        if not digits:
            return []
        number,digits = digits[0:1],digits[1:]   
        return helper(dict[number],digits)
```


簡化上面將產生第一個結果寫在helper 裡面
```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
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
                
        def helper(array,digits):        
            if digits:
                number,digits = digits[0],digits[1:]                
                result = []  
                if not array:#for first
                    return helper(dict[number],digits)                
                for s in array:
                    for letter in dict[number]:
                        result.append(s + letter)                
                return helper(result,digits)    
            return array            
     
        return helper([],digits)
```







