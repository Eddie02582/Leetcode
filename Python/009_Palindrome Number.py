'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''

class Solution:      
    def isPalindrome_simple(self, x):
        x = str(x)
        return True if x==x[::-1] else False     
    
    
    def isPalindrome(self, x):       
        x= str(x)     
        left,right = 0 , len(x)-1        
        mid = len(x) // 2 + len(x) %2
        
        while left < mid :
            if x[left] != x[right]:
                return False
            left, right= left+1 , right-1         
        return True
   
    def isPalindrome_res(self, x):
        if x < 0:
            return False   
        res,n=0,x
        
        while n:
            res = res*10 +n % 10
            n = n //10
        return res == x 
    
    def sPalindrome_div(self, x):      
        if x < 0:
            return False
        div = 1
        while x / div >= 10 :
            div *= 10
        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x % div) // 10
            div //= 100
        return True
      
sol =Solution()

assert sol.sPalindrome_div(121)==True

assert sol.isPalindrome_res(-121)==False

assert sol.isPalindrome_res(10)==False

assert sol.isPalindrome_res(1001)==True

assert sol.isPalindrome_res(12321)==True
