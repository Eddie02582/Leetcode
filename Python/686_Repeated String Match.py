'''
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (abcdabcdabcd), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

'''

class Solution(object):
    def repeatedStringMatch(self, A, B):        
        repeat = len(B) // len(A) + 2 
        for i in range(1,repeat + 1):
            if B in A * i:
                return i 
        return -1
        
        
        
sol = Solution()
assert sol.repeatedStringMatch('abcd',"cdabcdab") == 3    

assert sol.repeatedStringMatch('abc',"cabcabca") == 4 

assert sol.repeatedStringMatch('aa',"a") == 1 
 

assert sol.repeatedStringMatch("aaaaaaaaaaaaaaaaaaaaaab","ba") == 2 

        
        
        
        
        
