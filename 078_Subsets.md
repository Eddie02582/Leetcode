# Subsets

## 原題目:
```
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
```

參考
<a href = "https://leetcode.com/problems/subsets/solution/">Solution</a>

## 思路Cascading


#### Python
``` python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = [[]]
        
        for num in nums:
            temp = []
            for curr in output:
                temp.append(curr + [num])  
            output += temp
        return output
```


## 思路backtrack


#### Python
``` python
class Solution(object):
    def subsets(self, nums):
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()  
        return output
```


類似bitmask的想法,依序枚舉每個位置。針對每個位置，試著填入取或不取。

``` python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if first == n:  
                output.append(curr[:])
                return
            backtrack(first + 1, curr)
            backtrack(first + 1, curr + [nums[first]])             
        output = []
        visited  = [False] *len(nums)
        n = len(nums)
        backtrack()
        return output

```



## 思路bitmask


#### Python
``` python
class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output  
```







