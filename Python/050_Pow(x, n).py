'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [?231, 231 ? 1]
'''


class Solution:
    def myPow_buildin(self, x, n) :
        return x**n

    def myPow(self, x, n) :     
        if n <0:
            x = 1/x  
            
        result = 1        
        for i in range(1,abs(n) +1):
            result=result*x             
        return result
        
    def myPow(self, x: float, n: int) -> float:
        ret = 1
        tmp = abs(n)
        while(tmp):
            if tmp % 2 == 1:
                ret *= x
                tmp -= 1
            else:
                x *= x
                tmp /= 2
                
        return ret if n>0 else 1/ret        
        
        
        
sol =Solution()

assert sol.myPow(2,10)==1024        
        
assert sol.myPow(2,0)==1        
   
assert sol.myPow(2,-2)==0.25000      
        