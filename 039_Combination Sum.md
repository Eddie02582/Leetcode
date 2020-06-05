# Combination Sum

## 原題目:
```
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
      [7],
      [2,2,3]
    ]
Example 2:

    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
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
        def backtracking(array,start):
            if sum(array) == target:
                res.append(array[:])
                return
            elif sum(array) > target:
                return
            for i in range (start,len(candidates)): 
                n = candidates[i]              
                backtracking(array + [n],i)

        res = []    
        backtracking([],0)    
        return res        
           
``` 

簡化,使用sum稍微花點時間,這邊將每次的和也傳入

``` python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtracking(array,start,total):
            if total == 0 :
                res.append(array[:])
                return
            elif total < 0 :
                return
            for i in range (start,len(candidates)): 
                n = candidates[i]              
                backtracking(array + [n],i,total - n)

        res = []    
        backtracking([],0,target)    
        return res     
           
``` 












