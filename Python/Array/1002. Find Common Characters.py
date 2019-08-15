'''
Given an array A of strings made only from lowercase letters, return a 
list of all characters that show up in all strings within the list (including duplicates).  

For example, if a character occurs 3 times in all strings but not 4 times, you need to 
include that character three times in the final answer.

You may return the answer in any order.


Example 1:

    Input: ["bella","label","roller"]
    Output: ["e","l","l"]
Example 2:

    Input: ["cool","lock","cook"]
    Output: ["c","o"]

'''

class Solution(object):
    def commonChars_(self, A):
        array,result = [],[]
        for str in A:
            dict = {}
            for letter in str:
                dict[letter] = dict.get(letter,0) + 1
            array.append(dict)
        
        for letter in A[0]:
            appear = True
            for dict in array:
                if dict.get(letter,0) <=0:
                    appear = False
                else:
                    dict[letter] = dict.get(letter,0) - 1
            if appear:
                result.append(letter) 
        return result



sol = Solution()
assert sol.commonChars(["bella","label","roller"]) == ["e","l","l"]

assert sol.commonChars(["cool","lock","cook"]) == ["c","o"]