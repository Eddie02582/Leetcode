'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-2**31,  2**31-1 ].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

'''

class Solution:
    def reverse(self,x): 
    
        n=0    
        if x <0:
            flag = -1
        else:
            flag = 1
            
        x *= flag
        
        while x :            
            n = n * 10 + x % 10
            x = x // 10 
            
        return  n * flag if n <= 2**31-1 else 0

sol =Solution()

print (sol.reverse(123))

print (sol.reverse(-123))

print (sol.reverse(120))

print (sol.reverse(0))

print (sol.reverse(1534236469))