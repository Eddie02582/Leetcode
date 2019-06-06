
# encoding=utf-8
'''
476. Number Complement
Easy

Favorite

Share
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
    The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    You could assume no leading zero bit in the integer’s binary representation.
    
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.



Next challenges:

Bitwise AND of Numbers Range
Integer Replacement
IP to CIDR

'''


class Solution:
    def findComplement(self, num):        
        s=''.join([ '1'  if i=='0' else '0' for i in format(num,'b') ]) 
        return int(s,2)
        
    def findComplement_xor(self, num):
        n='1' *len(format(num,'b'))          
        return num ^ int(n,2)
        
        
        
sol =Solution()

assert sol.findComplement(5)==2