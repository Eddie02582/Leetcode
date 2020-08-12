# Minimum Size Subarray Sum


## 原題目:
```
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
```

## 思路two pointer
建立2個指針l,r,l表示subarray起始位置,r為結束位置,total 記錄subarray的和<br>
1.total +nums[r] (更新subarray和)<br>
2.檢查 total 是否大於目標値,(大於目標値需移動l產生subarray)<br>
    2.1 更新結果<br>
    2.2 移動l,更新total(新的subarray)<br>
3.移動r<br>



#### Python

``` python
class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0  
        
        l,r,total = 0,0,0
        ans = float('inf')

        while l <= r and  r < len(nums):
            total += nums[r]
            while total >= s:
                ans = min(ans,r - l + 1)
                total -= nums[l]
                l += 1  
            r += 1
     
        return  0 if ans == float('inf') else ans

``` 
