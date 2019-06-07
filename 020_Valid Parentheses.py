'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
        result=[]
        dict={')':'(','}':'{',']':'['}
        for x in s:
            if not result or x not in dict:
                result.append(x)
            elif dict[x]==result[-1]:
                result.pop()
            else:
                result.append(x)
        
        return result==[]
        
        
sol =Solution()

assert sol.isValid('()')==True

assert sol.isValid('()[]{}')==True

assert sol.isValid('((]')==False

assert sol.isValid('([)]')==False

assert sol.isValid('{[]}')==True

assert sol.isValid('}(')==False     
        
        
        
        
        
        
        
        