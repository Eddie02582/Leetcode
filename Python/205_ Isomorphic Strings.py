'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.


'''

class Solution:
    def isIsomorphic(self, s, t):
        dict={}
        for x,y  in zip(s,t):
            ##avoid ab aa
            if x not in dict and y not in dict.values():
                dict[x]=y     
            else:
                if dict.get(x,"")!=y:
                    return False   
        return True
        


sol =Solution()


assert sol.isIsomorphic("egg","add")==True

assert sol.isIsomorphic("foo","bar")==False

assert sol.isIsomorphic("paper","title")==True

assert sol.isIsomorphic("a","b")==True

assert sol.isIsomorphic("ab","aa")==False

assert sol.isIsomorphic("aa","ab")==False