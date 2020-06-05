# Combinations

## 原題目:
```
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

參考
<a href = "https://leetcode.com/problems/subsets/solution/">Solution</a>

## 思路backtrack


#### Python
``` python
class Solution(object):
    def combine(self, n, k):
        def backtrack(path, start):
            if len(path) == k:
                res.append(path)
            for i in range(start, n+1):
                backtrack(path + [i], i + 1)
        
        res = []
        backtrack([], 1)
        return res 
```


## 思路
python 內建itertools



#### Python
``` python
class Solution(object):
    def combine(self, n: int, k: int) -> List[List[int]]:
        import itertools
        x = itertools.combinations(range(1,n + 1), k)
        return x
```







