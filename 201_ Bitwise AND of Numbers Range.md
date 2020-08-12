#  Bitwise AND of Numbers Range


## 原題目:
```
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

    Input: [5,7]
    Output: 4
Example 2:

    Input: [0,1]
    Output: 0
```

## 思路1
迴圈作&運算,會TLE


#### Python

``` python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int: 
        ans = m
        for i in range(m + 1, n + 1):  
            ans &= i        
        return ans  
``` 

## 思路2


``` python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:    
       
        ans = 0
        for i in range(31,-1,-1):  
            dm =  m & (1 << i) 
            dn =  n &(1 << i)
            if dm != dn:
                return ans
            elif dm and dn:
                ans += 1 << i  
        
        return ans

```

