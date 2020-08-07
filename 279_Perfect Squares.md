# Perfect Squares


## 原題目:
```
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

## 思路
dp,先建立可以換的數字,就會變成coin change

#### Python

``` python
class Solution:
    def numSquares(self, n: int) -> int:
        coins = [ i * i for i in range(1, int(n**0.5) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
    
        for i in range(1, n + 1):
            dp[i] = min([1 + dp[i - coin] for coin in coins])          
        return dp[-1]     
``` 



``` python
    def numSquares_(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        p = 1
        while p * p <= n :
            dp[p * p] = 1
            p += 1
    
        for i in range(1, n + 1):
            p = 1
            while p * p <= i:
                dp[i] = min(dp[i - p * p] +dp[p * p],dp[i])    
                p += 1   
        return dp[-1]

``` 



