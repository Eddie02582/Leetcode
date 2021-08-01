# Multiply Strings

## 原題目:
```
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

```


## 思路backtracking


#### Python

``` python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        def backtracking(array,visited):
            if len(array) == len(nums):
                res.append(array[:])
                return         
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    backtracking(array + [nums[i]],visited)
                    visited[i] = False

        visited = [False] * len(nums)        
        res = []
        backtracking([],visited)
        return res   
``` 

## 思路2

``` python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]
        for num in nums:
            temp = []
            for sub in ans:
                for i in range(len(sub) + 1):
                    temp.append(sub[0:i]+[num]+ sub[i:])
            ans = temp[:]

        return ans
``` 
    
        
        