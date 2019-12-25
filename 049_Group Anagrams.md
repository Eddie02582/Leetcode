# Group Anagrams

## 原題目:
```
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
```

## 思路1
利用字典把結果存成下面這種型式,
```
{
   'aet':["ate","eat","tea"],
   'ant':["nat","tan"],
   'abt':["bat"]
}
```

#### Python

``` python
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
                result[t].append(s)      
        return result.values()    
``` 
 
類似的做法使用turple,結果存成下面這種型式,
```
{
   ('a','e','t'):["ate","eat","tea"],
   ('a','n','t'):["nat","tan"],
   ('a','b','t'):["bat"]


}
```

``` python
class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
```  


