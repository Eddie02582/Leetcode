# Reverse Integer


## 原題目:
```
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
```

## 思路1

1. 注意負數
2. 注意上限値
3. 用迴圈每次除以10 即可得到最後一位


## Code

#### Python

```python
class Solution:
    def reverse(self,x): 
    
        n=0    
        if x <0:
            flag = -1
        else:
            flag = 1
            
        x *= flag
        
        while x :            
            n = n * 10 + x % 10
            x = x // 10 
            
        return  n * flag if n <= 2**31-1 else 0
```



#### js
```javascript
var reverse = function(x) {
  
    var reverse = 0;    
    while(x)
    {
        reverse = reverse*10 + x%10;
        x = parseInt(x/10);
    }
    
    //return flag == true ? reverse : reverse*-1;
    if (reverse > 2**31 - 1 || reverse < -1*2**31)
        return 0
    return reverse 
};
```













