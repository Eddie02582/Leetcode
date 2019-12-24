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
    import collections
    #N*klogk
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]        
        """      
        ans = collections.defaultdict(list)        
        for s in strs:
            ans["".join(sorted(s))].append(s)
        return ans.values() 
        
    def groupAnagrams_turple(self, strs):       
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()  
        
    #N*k
    def groupAnagrams_array(self, strs): 
        ans = collections.defaultdict(list)
        for s in strs:
            s_key = [0] * 26
            for c in s:
                s_key[ord(c)-ord('a')] += 1
            ans[tuple(s_key)].append(s)
        return ans.values()
        
sol = Solution()
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol.groupAnagrams(a)