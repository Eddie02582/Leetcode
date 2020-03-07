# Palindrome Number


## 原題目:
```
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

    Input: 121
    Output: true
    
Example 2:

    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## 思路1
轉成字串,反轉比對


## Code

#### Python

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """ 
        
        return str(x) == str(x)[::-1]
```



#### js
```javascript
var isPalindrome = function(x) {
    return x == x.toString().split('').reverse().join('');
};
```

## 思路2
轉成整數判斷是否相等


## Code

#### Python

```python
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False   
        res,n=0,x
        
        while n:
            res = res * 10 +n % 10
            n = n //10
        return res == x   
```








