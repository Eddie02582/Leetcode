# Add Binary

## 原題目:
```
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

    Input: a = "11", b = "1"
    Output: "100"
    
Example 2:

    Input: a = "1010", b = "1011"
    Output: "10101"
```

## 思路1
字串長度不一樣,首先將字串長度弄成一樣,接下來就由後往前加,注意進位

#### Python

``` python
class Solution(object):
    def addBinary(self, a, b):        
        length = max(len(a),len(b))
        a = a.zfill(length)
        b = b.zfill(length)
        result = ""
        flag = 0
        
        for i in range(length - 1 , -1 , -1):
            total = int(a[i]) + int(b[i]) + flag
            n = total %2
            flag = total // 2            
            
            result = str(n) + result 
        
        if flag:
            result = "1" + result
        return result
``` 
## 思路2
利用雙指針m,n 紀錄陣列所在的index,由後往前,利用m,n是否大於-1,判斷該陣列是否走完,走完的陣列不相加

``` python
class Solution(object):
    def addBinary(self, a, b):   
        m,n = len(a) -1 ,len(b) -1
        p,flag = -1,0
        output=''
       
        while m > p or n > p:
            num = 0
            if m >p:
                num += int(a[m]) 
                m -= 1
            if n >p:
                num += int(b[n]) 
                n -= 1 
            
            flag , num = divmod( num + flag, 2)  
            output = str(num)+output
            
        return   "1" + output if flag else output
``` 
類似的作法,利用python 特性  a[-1] = a[len(a)] ,透過每次 p -=1 ,由後往前走,當p超過位置負長度(小於),表示該陣列已走完,直到a,b陣列結束  

``` python
class Solution(object):
    def plusOne(self, digits):        
        m,n =-len(a) ,-len(b)
        p,flag=-1,0
        output=''
        flag=0
        while p >= m or p >= n:
            num = 0
            if p>=m:
                num += int(a[p])
            if p>=n:
                num += int(b[p])  
            flag,num = divmod( num + flag, 2)                
            p -= 1  
            output = str(num)+output
            
        return   "1" + output if flag else output

``` 





