# Search in Rotated Sorted Array

## 原題目:
```
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
```

## 思路
先找到piviot的點,判斷是在哪一段再進行二分收尋法

## Code

#### Python

```python
class Solution(object):
    def search(self,nums,target):
        #find piviot index
        if len(nums) == 0:
            return -1

        length = len (nums) 
        l , r  = 0 , length - 1   
      

        while l != r:
            mid = l  + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid


        start = l
        if nums[start] <= target <= nums[- 1]:
            l , r = start , length - 1
        else:
            l ,r = 0 ,start - 1

        while l <= r:
            mid = l + (r - l ) // 2 
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
              
```




