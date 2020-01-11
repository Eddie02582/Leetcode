# 3Sum Closest


## 原題目:
```
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

## 思路1
題目沒說當num 長度小於3,要回傳什麼値,這邊假設長度至少為3
先排序,依次遍歷排序後的陣列,搭配雙指針l,r,l = i + 1, r = len(nums) -1,當總合比target 大,表示値比較大,將r 往左邊移,反之l往右邊移<br>


## Code

#### Python

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
        #-4 -1 1 2
        nums.sort()
        close_num = nums[0] + nums[1] + nums[2]      
        
        for i in range(len(nums) - 2 ):
            l , r = i + 1 , len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if  total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return target
            
                if abs(target - total) <  abs(target - close_num):
                    close_num = total
            
            
        return close_num

```







