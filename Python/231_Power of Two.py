'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

    Input: 1
    Output: true 
    Explanation: 2*0 = 1
    
Example 2:

    Input: 16
    Output: true
    Explanation: 2**4 = 16
    
Example 3:

    Input: 218
    Output: false

'''

class Solution(object):
    def isPowerOfTwo(self, n):      
        if n <= 0 :
            return False
            
        while n>1:
            if n % 2 != 0:
                return False
            n = n /2
        
        return True
        
    #2**x=n xlog2=logn x=logn/log2    
    def isPowerOfTwo_log(self, n):  
        from  math import log   
        return n > 0 and int(log(n)/log(2))== round(log(n)/log(2),10)   
        
    def isPowerOfTwo_div(self, n):             
        return n > 0 and 3**20 % n ==0 
        
    def isPowerOfTwo_bin(self, n):             
        return n >0 and bin(n).count('1')==1    
       
        
sol = Solution()

assert sol.isPowerOfTwo(0)==False

assert sol.isPowerOfTwo(-16)==False

assert sol.isPowerOfTwo(1)==True

assert sol.isPowerOfTwo(4)==True