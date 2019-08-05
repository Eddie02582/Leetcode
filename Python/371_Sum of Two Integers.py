'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

    Example 1:

    Input: a = 1, b = 2
    Output: 3
    
Example 2:

    Input: a = -2, b = 3
    Output: 1

'''

import ctypes



class Solution(object):
    def getSum(self, a, b):
        total = a ^ b
        carry = ctypes.c_int32(a & b)
        return self.getSum(total,carry.value << 1) if carry.value else total


    def getSum(self, a, b):       
        MAX = 0x7FFFFFFF        
        MIN = 0x80000000      
        mask = 0xFFFFFFFF
        while b != 0:            
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)


sol = Solution()

assert sol.getSum(1,4) == 5

assert sol.getSum(2,3) == 5