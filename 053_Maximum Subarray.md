# Maximum Subarray

## 原題目:
```
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.
```

## 思路1
利用雙指針i,j,i記錄擷取陣列開始位置,j為結束位置,每移動一次j,判斷總合是否最大値,當總合為負,即可離開,i往下走

#### Python

``` python
class Solution(object):
    def maxSubArray_normal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        for i in range(len(nums)):
            temp = 0
            j = i 
            while (temp >= 0 and j < len(nums)):
                temp += nums[j] 
                result = max(result,temp)
                j += 1

        return result 
``` 

## 思路1
 
用i歷遍整個陣列,當總合為負値表示需要重新計算,

#### Python
```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):            
            if temp < 0:
                temp = 0  
            temp += nums[i]             
            result = max(result,temp)  
        return result
```




