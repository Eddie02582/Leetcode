
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

#!/usr/bin/python
# encoding=utf-8
class Solution:
    def findComplement(self, num):        
        s=''.join([ '1'  if i=='0' else '0' for i in format(num,'b') ]) 
        return int(s,2)
        
    def findComplement_xor(self, num):
        n='1' *len(format(num,'b'))          
        return num ^ int(n,2)
    
    #bin(5)=101
    # 2 = 0b101 ^0b111
    # 0b111 =0b1111-1
    # 所以將 b>>位數 -1 即可以得到要xor 的數字
    def findComplement_xor_not_bin(self, num):
        a = num
        b = 1
        while a:
            a = a >> 1            
            b =b << 1         
        return num ^ (b-1)
    
    #簡化上面
    def findComplement_xor_simplify(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num       
        
        
sol =Solution()

assert sol.findComplement(5)==2