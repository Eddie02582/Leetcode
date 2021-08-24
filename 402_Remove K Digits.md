# Remove K Digits


## 原題目:
```
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all the digits from the number and it is left with nothing which is 0.
```


## 思路
利用stack的概念,歷遍整個num,迴圈判斷int(num[i]) > int(num[i + 1]) 和count = k 符合,將堆疊的值移出<br>
最後移除頭是"0",如果count 不足,最後砍掉尾巴補足
 
```
ex :"1432219" 

當 s = 1  => stack = [1]
當 s = 4  => stack = [1,4]
當 s = 3  => check stack[-1] > 3 => stack = [1] => check stack[-1] > 3 => stack = [1,3] 
當 s = 2  => check stack[-1] > 2 => stack = [1,2] 
當 s = 2  => check stack[-1] > 2 => stack = [1,2]
當 s = 2  => check stack[-1] > 2 => stack = [1,2,2]
當 s = 1  => check stack[-1] > 1 => stack = [1,2] =>stack = [1,2,1]
當 s = 9  => check stack[-1] > 9 => stack = [1,2,1,9]
```
#### Python

``` python
    def removeKdigits(self,num,k):
        if len(num) <= k:
            return '0'
        stack = []
        
        for n in num:               
            while stack and k and int(stack[-1]) > int(n):
                stack.pop(-1)
                k -= 1            
            stack.append(n)          
  
        while k :
            stack.pop(-1)
            k -= 1
            
        while len(stack) >1 and stack[0] == '0':
            stack.pop(0)        
        
        return "".join(stack) 
``` 

簡化


```
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        stack = []
        remain = len(num) - k
        
        for n in num:              
            #stack[-1] > n euqla ord('stack[-1]') > ord(n)
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1            
            stack.append(n)        
  
        return ''.join(stack[:remain]).lstrip('0') or '0'

```

