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
這題思路類似於Next Permutation,我們將高位數字降低,希望替補上來的元素値比較小,所以拿掉由高位非升序排序的前一個值
```
ex :"1432219" k= 3
當 k = 1 => 1,4,3　拿掉4(3比4小) => 132219
當 k = 2 => 1,3,2　拿掉2(2比3小) => 12219
當 k = 3 => 1,2,2,1　拿掉1(1比2小) => 1219

```
利用count 記錄移除個數,迴圈歷遍num,當遇到int(num[i]) > int(num[i + 1]),count += 1,更新新的num<br>
注意當迴圈結束時count < k,則把尾巴砍掉


#### Python

``` python
class Solution:
    def removeKdigits(self,num,k):
        if k > len(num):
            return "0"

        count = 0        
        while count < k and num:      
            isFind = False
            for i in range(len(num) - 1):
                if int(num[i]) > int(num[i + 1]):
                    isFind = True
                    num = num[0 : i] + num[i + 1:]
                    count += 1
                    break
            if not isFind:
                break
        while  count < k and num:         
            num = num[0:-1]
            count += 1   
        if not num:
            return "0"

        return str(int(num))    
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
        if k > len(num) or not num:
            return "0"

        stack,count = [],0        
 
        for s in num:           
            n = int(s)
            while stack and int(stack[-1]) > n and count < k:
                stack.pop()
                count += 1                  
            stack.append(s) 

        while stack and stack[0] == "0":
            stack.pop(0)

        while stack and count < k:
            count += 1
            stack.pop()
    
        return "".join(stack) if stack else "0"

``` 



