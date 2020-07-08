# Combination Sum II

## 原題目:
```
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

```



## 思路backtracking


#### Python




``` python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtracking(array,start,total):
            if total == target :
                res.add(tuple(array[:]))
                return
            elif total > target :
                return
            for i in range (start,len(candidates)): 
                n = candidates[i]              
                backtracking(array + [n],i + 1,total + n)

        res = set()
        candidates.sort()
        backtracking([],0,0)    
        return res
           
``` 
## 思路DP

``` python
class Solution(object):
    def combinationSum(self, candidates, target):              
        from collections import defaultdict
        dp = defaultdict(set)
        candidates.sort()
        dp[0].add(())
        for n in candidates:
            for i in range(n, target + 1):                
                for seq in dp[i - n]:
                    dp[i].add(seq+(n,))
        return dp[target]       
           
``` 










