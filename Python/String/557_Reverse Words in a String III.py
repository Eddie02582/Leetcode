'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

    Example 1:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

'''


class Solution:

    def reverseWords(self, s: str) -> str:
        result = []
        for word in s.split():  
            result.append(word[::-1])    
           
        return ' '.join(result)       

        
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = ''
        for i in range(len(words)):  
            ans = ans + words[i][::-1]
            if i != len(words)- 1:
                ans += " "           
        return ans  

    def reverseWords_(self, s: str) -> str:
        words = s.split()
        ans = ''
        for i in range(len(words)):           
            r = len(words[i]) - 1
            while r >= 0:
                ans +=  words[i][r]
                r -= 1
            if i != len(words)- 1:
                ans += " "           
        return ans
