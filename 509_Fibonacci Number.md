# Find All Duplicates in an Array


## 原題目:
```
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

 

Example 1:
    Input: 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
    
Example 2:
    Input: 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
    
Example 3:
    Input: 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

## 思路遞回
將題目寫成遞迴


#### Python

``` python
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        else:
            return self.fib(N - 1) +  self.fib(N -2)       
``` 



## 思路 動態規劃Bottom-Up


``` python
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        
        table = [0]* (N + 1)
        table[1] = 1
        
        for i in range(2,N + 1):
            table[i] = table[i - 1] +table[i - 2]
        return table[N]
``` 



## 思路 動態規劃Top-Down

動態規劃

``` python
class Solution:    
 
    def fib(self, N: int) -> int:       
        if N <= 1:
            return N    

        table  = [0] * (N  + 1)
        table[1] = 1    

        for i in range(0,N  + 1):
            if i + 1 <= N :
                table[i + 1] += table[i]
            if i + 2 <= N :
                table[i + 2] += table[i]  
        return table[N] 

```

``` python
class Solution:
    def fib(self, N: int) -> int:
class Solution:    
    def fib(self, N: int) -> int:       
        if (N <= 1):
            return N
        current = 0
        prev1 = 1  #f(1)
        prev2 = 0  #f(0)   
     
        for i in range(2, N+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current
```












