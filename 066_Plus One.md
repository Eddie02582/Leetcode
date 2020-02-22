# Plus One

## 原題目:
```
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    
Example 2:

    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
```

## 思路
由後往前歷遍,使用flag 判斷是否有進位,如果迴圈完flag不是0,則要把flag 插入最前面

#### Python

``` python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        flag = 1
        for i in range(length-1,-1,-1):  
            n = digits[i] + flag
            digits[i] = n % 10
            flag = n //10
        
        if flag:
            digits.insert(0,flag)
        
        return digits
``` 

使用內建函數divmod
``` python
class Solution(object):
    def plusOne(self, digits):        
        flag = 1
        length = len(digits)
        for i in range(length-1,-1,-1):                       
            flag,digits[i] =  divmod(digits[i] + flag,10)                
        if flag:
            digits=[flag]+digits       
        return digits
``` 





