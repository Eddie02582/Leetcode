'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

    Input: 4
    Output: 2
    
Example 2:

    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since 
                 the decimal part is truncated, 2 is returned.
             
'''


class Solution(object):
    def mySqrt_build(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x**0.5)
    '''
    y**2=x
    logy**2=logx
    2logy=logx
    y=10**(0.5*logx)
    '''
    def mySqrt_log(self, x):
        import math 
        if x==0 :
            return 0
        
        return int( 10**(0.5 *math.log10(x)))
     
    #Using Newton's method:
    def mySqrt(self, x):
        result = 1
        if x == 0 :
            return 0
        while abs(result * result - x) >0.1:
            result=(result + float(x) / result) /2
        return int(result)        

    #Binary
    def mySqrt(self, x):
        r = x
        l = 0
        while l < r:
            mid =(l + r)//2
            if  mid**mid < x:
                l = mid + 1
                  
    

      
    
sol =Solution()

assert sol.mySqrt(4)==2

assert sol.mySqrt(8)==2

assert sol.mySqrt(1)==1

assert sol.mySqrt(0)==0