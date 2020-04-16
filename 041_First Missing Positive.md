# First Missing Positive

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
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums) + 1):
            if i not in nums:
                return i
        
        return len(nums) + 1   
``` 
## 思路2
解這題就是要掃描這個矩陣，然後把值為i+1的元素放到第i個位置，
有一些越界的狀況(例如nums[i]=-1)，那我們就直接跳過。
完成後再一次掃過該矩陣，若第i個元素不等於i+1，i+1就是我們要找的解，


``` python
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        for i in range(n):
            while nums[i] > 0 and  nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index],nums[i]            
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1;
        
        return len(nums) + 1


```










