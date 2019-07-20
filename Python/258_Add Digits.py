'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
'''

class Solution(object):
    def addDigits_loop(self, num):
        while num >9:
            total = 0
            while num:                
                total += num%10
                num = num //10
            num = total
        return num        

    def addDigits_res(self, num):
        if num < 10:
            return num
        else:
            total = 0
            while num:                
                total += num%10
                num = num //10
            num = total    
        return self.addDigits(num)
    

    def addDigits(self,n):
        return n if n < 10 else self.addDigits(sum(map(int,str(n))))
                







     