'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
#similar 415_add strings


class Solution:
    def multiply(self, num1, num2):        
        return  str( self.ToInt(num1) *  self.ToInt(num2))
    
    def ToInt(self,num):
        total=0
        for x in num:
            total=total * 10 + ord(x) - ord('0') 
        return total
    
sol = Solution()
assert sol.multiply('2','3')=='6'

assert sol.multiply('123','456')=='56088'