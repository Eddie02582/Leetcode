# Remove Duplicates from Sorted Array

## 原題目:
```
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```

## 思路
用指針記錄當前位置,迴圈所有nums値,當値不等於指針當前位置的值,指針向右移動,並將値寫入指針位置

## Code

#### Python

```python
class Solution(object):
    def removeDuplicates(self, nums):
        
        if nums == []:
            return 0
        
        p = 0
        for n in nums:
            if n != nums[p]:
                p += 1
                nums[p] = n
        return p + 1
```







