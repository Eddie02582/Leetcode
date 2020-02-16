# Multiply Strings

## 原題目:
```
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

    Input: num1 = "2", num2 = "3"
    Output: "6"
    
Example 2:

    Input: num1 = "123", num2 = "456"
    Output: "56088"
    
Note:

    1.The length of both num1 and num2 is < 110.
    2.Both num1 and num2 contain only digits 0-9.
    3.Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    4.You must not use any built-in BigInteger library or convert the inputs to integer directly.


```


## 思路1





#### Python

``` python
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """        
    
        def strToInt(s):
            num = 0
            for p in s:
                num = num *10 + ord(p) -48
            return num
        
        return str(strToInt(num1) * strToInt(num2))
``` 


