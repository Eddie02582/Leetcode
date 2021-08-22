'''
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

Example 1:
    Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16
    Explanation: The two words can be "abcw", "xtfn".
    
Example 2:
    Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
    Output: 4
    Explanation: The two words can be "ab", "cd".
    
Example 3:
    Input: words = ["a","aa","aaa","aaaa"]
    Output: 0
    
Explanation: No such pair of words.

Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
'''


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        S = list(map(set, words))
        
        for i in range(len(words) - 1):
            for j in range(i + 1,len(words)):
                if not S[i] & S[j]:
                    ans = max(ans,len(words[i]) * len(words[j]))
        
        
        return ans
        
    def maxProduct(self, words: List[str]) -> int:        
        bitmask, ans = [], 0
        for word in words:
            bitmask.append(0)
            for c in word:
                bitmask[-1] |= 1 << (ord(c) - ord('a'))
        for i in range(len(words)):
            for j in range(i):
                if bitmask[i] & bitmask[j] == 0:
                    ans = max(ans, len(words[i] * len(words[j])))
        return ans