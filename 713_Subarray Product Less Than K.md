# Subarray Product Less Than K


## 原題目:
```
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
    Input: nums = [10, 5, 2, 6], k = 100
    Output: 8
    Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Note:

    0 < nums.length <= 50000.
    0 < nums[i] < 1000.
    0 <= k < 10^6.
```

## 思路雙重迴圈
迴圈遍歷,l表示啟始位置,j表示結束位置,每次一動j將上次結果相乘,値小於k,count += 1


#### Python
``` python
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """      
        count = 0
        for l in range(len(nums)): 
            total = 1
            for r in range(l,len(nums)):                
                total *= nums[r]
                if total < k:
                    count += 1
                else:
                    break    
        return count 
``` 



## 思路 雙重指針
1.product 一開始是 1，ans 一開始是 0 <br>
2.假設一開始左指針指向 10，右指針也指向 10，這時候 product *= 10 ,此時有[10]符合(r - l + 1)<br>
3.右指針也指向 5，這時候 product *= 5 ,producy = 50 ,此時有[10,5],[5]符合(r - l + 1)<br>

直到product > k，那就得把 product /= 左手指向的值，並把左手往右移，直到 product < k，這時就又可以再把 ans += (r-l+1)<br>


``` python
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
      
        if k <= 1:
            return 0
      
        count ,product ,l = 0,1,0
        for r in range(len(nums)): 
            product *= nums[r]
            while product >= k:
                product //= nums[l];
                l += 1
            count += r - l + 1;  
        return count    
``` 














