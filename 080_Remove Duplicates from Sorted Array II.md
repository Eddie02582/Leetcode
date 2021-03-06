# 80. Remove Duplicates from Sorted Array II

## 原題目:
```
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

    Given nums = [1,1,1,2,2,3],

    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

    It doesn't matter what you leave beyond the returned length.

Example 2:

    Given nums = [0,0,1,1,1,1,2,3,3],

    Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

    It doesn't matter what values are set beyond the returned length.
```

## 思路


#### Python



``` python
class Solution(object):
    def removeDuplicates(self, nums):  
        p ,count = 0,0
        for n in nums:   
            count += 1
            if p and nums[p - 1] != n:               
                count = 1               
            if count <= 2:
                nums[p] = n  
                p += 1            
        return p
``` 


## 思路2

#### Python



``` python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 2
        if len(nums) <3:
            return len(nums)
        for i in range(2, len(nums)):
            if nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index +=1
        return index     
``` 




