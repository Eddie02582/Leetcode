# Implement strStr()

## 原題目:
```
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:
    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = truncate(3.33333..) = 3.
    
Example 2:
    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = truncate(-2.33333..) = -2.
    
Note:
    Both dividend and divisor will be 32-bit signed integers.
    The divisor will never be 0.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
```

## 思路
不能用乘法這邊使用加法一步一步累加,但是這樣會timeout<br>


## Code
<a href = "https://www.jianshu.com/p/982d1f0ea98d">參考</a>
#### Python

```python
class Solution(object):
    def divide(self, haystack, needle):        
        if not divisor or (dividend == -2**31 and divisor == - 1) or (dividend == 2**31 and divisor == 1):
            return 2**31 - 1
        
        result = 0
        sign =  dividend * divisor < 0 
        dividendabs  = abs(dividend)
        divisorabs  = abs (divisor)
        while divisorabs <= dividendabs:
            temp ,doubles = divisorabs ,1   
            while (temp << 1) <= dividendabs:
                temp <<= 1
                doubles <<= 1            
            dividendabs -= temp;
            result += doubles;
        return  - 1 * result  if sign  else result  
```

## 思路

<a href = "https://knightzone.studio/2018/10/24/3944/leetcode%EF%BC%9A29-divide-two-integers/">參考</a>

```python
class Solution(object):
    def divide__shift(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if not divisor or (dividend == -2**31 and divisor == - 1) or (dividend == 2**31 and divisor == 1):
            return 2**31 - 1

        dividendabs  = abs(dividend)
        divisorabs  = abs (divisor)        
        maxShiftDigit = 0
        while  divisorabs << maxShiftDigit <= dividendabs:
            maxShiftDigit += 1

        sign,result  =  dividend * divisor < 0,0

        for i in range(maxShiftDigit - 1 , - 1 ,-1):
            shiftValue = divisorabs << i
            if shiftValue <= dividendabs:
                result += (1 << i);
                dividendabs -= shiftValue;

        return  - 1 * result  if sign  else result      
```


