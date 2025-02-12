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
利用字典把結果存成下面這種型式,將每個字串重新排序當作字典的key,即可用key分類
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


```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (const string &s : strs) {  
            string key = s;
            sort(key.begin(), key.end());
            mp[key].push_back(s); 
        }
        vector<vector<string>> result;
        for (const auto &pair : mp) {  
            result.push_back(pair.second);
        }
        return result; 
    }
};
```

優化
1.use auto& rather then auto to avoid unnecessary copy<br>
2.use std::move() to steal vector from map<br>
3.use vector.reserve() to avoid reallocate<br>

```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();
        unordered_map<string, vector<string>> map;
        vector<vector<string>> ret;
        for (const auto& s : strs) {
            string t = s;
            sort(t.begin(), t.end());
            map[t].push_back(s);
        }
        ret.reserve(map.size());
        for (auto& p : map) {
            ret.push_back(std::move(p.second));
        }
        return ret;
    }
};
```








