'''
67. Add Binary


Share
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
#!/usr/bin/python
class Solution:
    ##利用python 從indxe -1 and -length,注意判斷溢位
    def addBinary_(self, a,b):
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
            flag,num = divmod( num+flag, 2)                
            p -= 1  
            output=str(num)+output
            
        return   "1" + output if flag else output
    ##normal solution
    def addBinary(self, a,b):
        m,n =len(a)-1 ,len(b)-1
        flag,num=0,0
        output=''
        while m >= 0  or n >= 0:
            num = 0
            if m >=0 :
                num += int(a[m])
            if n >=0:
                num += int(b[n])
            flag,num = divmod( num+flag, 2)
          
            m ,n =m-1 , n-1

            output=str(num)+output
            
        return   "1" + output if flag else output



sol =Solution()

assert sol.addBinary('11','1')=='100'

assert sol.addBinary('1010','1011')=='10101'