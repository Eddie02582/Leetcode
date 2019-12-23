'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        result = {}
        for s in strs:
            t = "".join(sorted(s))
            if t not in result:
                result[t] = [s]
            else:
                result[t] = result[t]+[s]
        print (result.values())
        result = list(sorted(result.values()))
        for i in range(len(result)):
            result[i] = sorted(result[i])
 
        return result
        
        
sol = Solution()
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol.groupAnagrams(a)