'''
Share
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.
Example 2:

    Input: "aba"
    Output: False
Example 3:

    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''


##similar 043_Multiply Strings


class Solution(object):
    def repeatedSubstringPattern(self, s):
        head = s[0]
        for i in range(1,len(s)//2+1):
            if s[i] == head and s[0:i] == s[i:2*i]:
                same = True
                for j in range(2 * i,len(s),i): 
                    if head != s[j] or s[0:i] != s[j:j + i]:
                        same = False
                        break
            
                if same:
                    return True
        return False




sol =Solution()
assert sol.repeatedSubstringPattern ('abab')== True

assert sol.repeatedSubstringPattern ('aba')== False

assert sol.repeatedSubstringPattern ('abcabcabcabc')== True

assert sol.repeatedSubstringPattern ('1234112341')== True

assert sol.repeatedSubstringPattern ('12341123411234112341')== True

assert sol.repeatedSubstringPattern ('ababba')== False
