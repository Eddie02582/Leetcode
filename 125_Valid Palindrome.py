'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true
    
Example 2:

    Input: "race a car"
    Output: false
'''

class Solution(object):
    def isPalindrome(self, s):    
        l,r=0,len(s)-1
        s = s.lower()
        while l < r :
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l] !=s[r]:
                    return False
                l += 1
                r -= 1
        return True
        
    def isPalindrome_reverse(self, s: str) -> bool:
        s=''.join(i.lower() for i in s if i.isalnum()==True)
        return s==s[::-1]        
        
        
sol =Solution()
assert sol.isPalindrome("A man, a plan, a canal: Panama")==True

assert sol.isPalindrome("race a car")==False

assert sol.isPalindrome("OP")==False