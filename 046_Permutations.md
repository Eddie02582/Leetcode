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
1. num = 1,此時ans = [[]] => 對於每個ans插入不同的位置 =>temp[[1]]
2. num = 2 此時ans = [[1]] => 對於每個ans插入不同的位置 
    [1] => [1,2],[2,1] 
3. num = 3 此時ans = [[1]]=> 對於每個ans插入不同的位置 
    [1,2] => [3,1,2],[1,3,2],[1,2,3]
    [2,1] => [3,2,1],[2,3,1],[2,1,3]



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

遞迴版本
``` python
class Solution:
    def permute(self, nums: List[int],res = [[]]) -> List[List[int]]:    
        def permutation(nums,res):   
            if not nums:
                return res
            length = len(res)
            
            while length > 0:            
                sub = res.pop(0)            
                for j in range(len(sub) + 1): 
                    res.append(sub[0:j] + [nums[0]] + sub[j:])                 
                length -= 1        
            return permutation(nums[1:],res)
        return permutation(nums,[[]])
``` 

## 思路3


``` python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        ans = []
        def permutation(nums,prefix):    
            if not nums:
                ans.append(prefix[::])
            else:
                for i in range(len(nums)):
                    rem = nums[0:i] + nums[i + 1:]
                    permutation(rem,prefix + [nums[i]])           
        
        permutation(nums,[])
        return ans
```
        
        
        
        
        
        
        
        
        
        
        
        
        
        