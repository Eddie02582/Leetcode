# Permutations II

## 原題目:
```
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

```


## 思路backtracking


#### Python

``` python
class Solution:
    def permuteUnique(self, nums):        
        def backtracking(array,visited):
            if len(array) == len(nums):
                res.add(tuple(array[:]))
                return         
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    backtracking(array + [nums[i]],visited)
                    visited[i] = False

        visited = [False] * len(nums)        
        res = set()
        backtracking([],visited)
        return res
``` 


