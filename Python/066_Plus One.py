'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
Example 2:

    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.

'''


class Solution(object):
    def plusOne_divmod(self, digits):        
        flag=1
        for i in range(len(digits)-1,-1,-1):                         
            flag,digits[i] =  divmod(digits[i] + flag,10)                
        if flag:
            digits=[flag]+digits       
        return digits
        
    def plusOne(self, digits):        
        flag=1
        for i in range(len(digits)-1,-1,-1):  
            digits[i] = digits[i] + flag             
            flag = digits[i] //10
            digits[i] = digits[i]%10                 
        if flag:
            digits=[flag]+digits  
   
        return digits
                
        
        
        
    
sol =Solution()

assert sol.plusOne([1,2,3])==[1,2,4]   

assert sol.plusOne([9,9])==[1,0,0]         
        
        
