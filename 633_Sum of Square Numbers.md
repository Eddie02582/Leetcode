# Average of Levels in Binary Tree

## 原題目:
```
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:
    Input: c = 5
    Output: true
    Explanation: 1 * 1 + 2 * 2 = 5
    
Example 2:
    Input: c = 3
    Output: false
    
Example 3:
    Input: c = 4
    Output: true
    
Example 4:
    Input: c = 2
    Output: true
    
Example 5:
    Input: c = 1
    Output: true 
```

## 思路hash set
先將所有可能的平方存在hash set,最後在loop 找尋 c- a *a 的值



#### Python
``` python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        for i in range(0,int(c**0.5)+1):
            squares.add(i * i)
        
        for square in squares:
            if (c - square) in squares:
                return True           
        return False 
``` 


## 思路loop 檢查sqrt 是否為整數

這邊使用sqrt函數會比**0.5快


``` python
from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = sqrt(c - a * a);
            if b == int(b):
                return True  
            a += 1
        return False 
 ```


## two pointer


``` python
class Solution:        
    def judgeSquareSum(self, c: int) -> bool:
        l,r = 0, int(c **0.5)
        while l <= r:
            value = l * l + r * r
            if value == c:
                return True
            elif value > c:
                r -= 1
            else:
                l +=1  
        return False 
        
 ```







