# Search Insert Position

## 原題目:
```
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

    Input: [1,3,5,6], 5
    Output: 2
    
Example 2:

    Input: [1,3,5,6], 2
    Output: 1

Example 3:

    Input: [1,3,5,6], 7
    Output: 4
    
Example 4:

    Input: [1,3,5,6], 0
    Output: 0
```

## 思路

## Code
迴圈歷遍當値大於target時回傳i
#### Python

```python
class Solution(object):
    def searchInsert(self, nums, target):        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i 
        return len(nums)
         
```

## 思路2
使用二分收尋法
```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l,r = 0 ,len(nums) - 1             
       
        while l <=  r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: 
                r = mid - 1
            else:
                l = mid + 1
        
        return l
```
