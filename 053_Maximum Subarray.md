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
dp[i] = max(dp[i - 1] + nums[i],nums[i])

#### Python

``` python
class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        ans = nums[0]
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i - 1] + nums[i],nums[i])
            
            ans = max(ans,dp[i])
        
        return ans
``` 

簡化若前面的和加上當前的值比當前的值小,更新和為當前的值

#### Python
```python
class Solution(object):        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prev = nums[0]     
        ans = nums[0]
        
        for i in range(1,n):
            prev = max(prev+ nums[i],nums[i])            
            ans = max(ans,prev)        
        return ans
```
#### c++

```c++
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0];
        int temp = nums[0];
        
        for(int i = 1;i < nums.size();i++){
            temp += nums[i];
            if(temp < nums[i])
                temp = nums[i];
            if(temp > ans)
                ans = temp;            
        }
        
        return ans;  
    }
    
};

```
## 思路2(類似的做法)
當值小於0加上原本的值一定比原本值小,所以當值小於0,直接將和歸0

#### Python

<a href = "https://leetcode.com/problems/maximum-subarray/submissions/">97.38</a>
```python
class Solution(object):   
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')      
        temp = 0
        for n in nums:
            if temp < 0:
                temp = 0
            temp += n
            ans = max(temp,ans)
        
        return ans
```

#### c++

```c++
class Solution {
public:    
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0];
        int temp = 0;
        
        for(auto n : nums){           
            if(temp < 0)
                temp = 0;
            temp += n;
            if(temp > ans)
                ans = temp;            
        }
        
        return ans;  
    } 
};
```






