'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

'''

class Solution:
    def convertToTitle(self,n):
        
        res = ''
        while n:
            res = chr((n - 1) % 26 + 65) + res
            n = (n - 1) / 26
        return res


    def convertToNumber(self,col_name):
        total = 0
        for letter in col_name:
            total *= 26
            total += ord(letter)- ord('A') + 1
        return  total
    
sol= Solution()

assert sol.convertToTitle(3) == "C"

assert sol.convertToTitle(28) == "AB"

assert sol.convertToTitle(701) == "ZY"

# assert sol.convertToTitle(702) == "ZZ"

assert sol.convertToNumber('ZZ') == 702