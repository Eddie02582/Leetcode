# Jump Game

## 原題目:
```
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
```

## 思路
迴圈歷遍,記錄當下能走到最大的位置max_loc,如果i > max_loc,表示不可能走到,如果max_loc大於len(nums) - 1表示可以走到最後,每次更新max_loc


#### Python

``` python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False    
        
        max_loc = 0        
        for i in range(len(nums)):
            if i > max_loc:
                return False
            if max_loc >= len(nums) - 1:
                return True            
            max_loc = max(max_loc,nums[i] + i)
        return True
``` 

``` python

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False    
        
        max_loc = 0        
        for i in range(len(nums)):
            if i > max_loc:
                return False
            if max_loc >= len(nums) - 1:
                return True            
            max_loc = max(max_loc,nums[i] + i)
        return True



```


## 思路


#### Python
``` python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start, end = 0, 0
        while end < len(nums) - 1:
            start, end = end, max(i + nums[i] for i in range(start, end + 1))
            if start == end: return False
        return True
```
















