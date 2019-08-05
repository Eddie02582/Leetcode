'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''


##similar 043_Multiply Strings

class Solution:
    def addStrings2(self, num1: str, num2: str) -> str:
        return str(self.ToInt(num1)+self.ToInt(num2))

    def ToInt(self,num):
        total=0
        for x in num:
            total=total * 10 + ord(x) - ord('0') 
        return total
        
        
    def addStrings(self, num1: str, num2: str) -> str:
        p ,flag =-1,0
        msg=""
        
        while p >= -len(num1) or p >= -len(num2) :
            n=0
            if p >=-len(num1):
                n += ord(num1[p]) - 48
            if p >=-len(num2):
                n += ord(num2[p]) - 48 
                
            flag,n=divmod(n+flag,10)
            msg = str((n))+ msg 
            p -= 1        
        return  "{}{}".format(flag,msg) if flag else msg
        


sol =Solution()
assert sol.addStrings ('1','1')=='2'


assert sol.addStrings ('110','2')=='112'

assert sol.addStrings ('120','91')=='211'