# Group Anagrams

## 原題目:
```
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

    Input: [1,2,0]
    Output: 3

Example 2:

    Input: [3,4,-1,1]
    Output: 2

Example 3:

    Input: [7,8,9,11,12]
    Output: 1ft 3x3 sub-box, it is invalid.



```


## 思路1
從i = 1開始比對, 若值不在陣列則回傳,在則i = i+1




#### Python

``` python
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while True:
            if(i not in nums):
                return i
            i += 1
           
``` 

用for 
``` python
class Solution(object):
    def firstMissingPositive(self, nums):
        length = len(nums)
        for i in range(1,length + 1):
            if i not in nums:
                return i
        
        return length
           
``` 

