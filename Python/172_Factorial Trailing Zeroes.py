'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

    Input: 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.
    
Example 2:

    Input: 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.

'''

class Solution(object):
    def trailingZeroes_count(self, n):
        total = factorial(n)
        count = 0
        while not total % 10:            
            count += 1           
            total = total//10
        return count
        
    def trailingZeroes_res(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)        
        
         
    def trailingZeroes(self, n):
        res = 0
        while n :
            res += n//5
            n //= 5
        return res
            
        
from functools import reduce
def factorial(n):
    total = 1
    for i in range(2,n+1):
        total = total * i
    return total


sol = Solution()

assert sol.trailingZeroes(3) == 0
assert sol.trailingZeroes(5) == 1
assert sol.trailingZeroes(25) == 6

