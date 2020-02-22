# Climbing Stairs

## 原題目:
```
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    
Example 2:

    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
```

## 思路
以4階為例,爬4階只能從3階和2階爬上,爬3階只能從2階和1階爬上,爬2階只能從1階和0階爬上<br>
所以簡單來說是f[0] = 1 的費氏數列
``` 
    f[0] = 1
    f[1] = 1
    f[n] = f[n-1] + f[n-2] n>=2
```

#### Python

遞迴的寫法,但是這樣會重複計算
``` python
class Solution(object):
    def climbStairs(self, n):   
        if n == 0 or n == 1:
            return 1
        else:
            return climbStairs(n-1) + climbStairs(n-2)
``` 

遞迴但使用table紀錄計算的值
``` python
class Solution(object):

    def climbStairs_top_down(self, n):  
        table = [0] *(n + 1)
        
         if n == 0 or n == 1:
            return 1
            
        if table[n] != 0:
            return table[n]
            
        table[n] =  self.climbStairs(n-1) + self.climbStairs(n-2)
        return table[n] 
```



動態規劃(buttom Up)
``` python
class Solution(object):
    def climbStairs(self, n):        
        f = [0] *(n + 1)
        f [0] = 1
        f [1] = 1
        for i in range(2,n + 1):
            f[i] = f[i - 1] + f[i - 2]  
        return f[n]
``` 

動態規劃
``` python
class Solution(object):
    def climbStairs(self,n):
        table = [0] *(n + 1) 
        table[0]=1
 
        for i in range(0,n+1):
            if i + 1 <= n:
                table[i+1] += table[i]
            if i + 2 <= n:
                table[i+2] += table[i]
        return table[n]

``` 

















