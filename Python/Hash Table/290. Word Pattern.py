'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

    Input: pattern = "abba", str = "dog cat cat dog"
    Output: true
    
Example 2:

    Input:pattern = "abba", str = "dog cat cat fish"
    Output: false
    
Example 3:

    Input: pattern = "aaaa", str = "dog cat cat dog"
    Output: false
    
Example 4:

    Input: pattern = "abba", str = "dog dog dog dog"
    Output: false
'''


class Solution(object):
    def wordPattern(self, pattern, str):        
        words = str.split()
        if len(pattern) != len(words):
            return False
            
        dict = {}
        for word,letter in zip(words,pattern):
            if word not in dict:
                if letter not in dict.values():
                    dict[word] = letter 
                else:
                    return False
            elif dict[word] != letter:
                return False             
            
        return True
            
            
sol = Solution()           
str = "dog cat cat dog"
assert sol.wordPattern('abba',str) == True   
assert sol.wordPattern('abba',"dog cat cat fish") == False   
assert sol.wordPattern('aaaa',str) == False   
assert sol.wordPattern('abba',"dog dog dog dog") == False   











      
            