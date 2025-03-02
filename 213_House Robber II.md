# House Robber


## 原題目:
```
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1:
	Input: nums = [2,3,2]
	Output: 3
	Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
	
Example 2:
	Input: nums = [1,2,3,1]
	Output: 4
	Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
	Total amount you can rob = 1 + 3 = 4.
Example 3:
	Input: nums = [1,2,3]
	Output: 3
	
Constraints:
	1 <= nums.length <= 100
	0 <= nums[i] <= 1000
	
```

## 思路 dp
與Robber一樣 ,只是變成環形,所以當搶第一個,最後一個就不能搶,反之,所以拆成1個nums去解,再取出max



#### C++

```c++
class Solution {
public:
    int rob(vector<int>& nums) {       
        int n = nums.size();
        if (n == 0) return 0;  // 空数组
        if (n == 1) return nums[0]; // 只有一个房子
        
        vector<int> nums1(nums.begin(), nums.end() - 1);  // 不抢最后一间
        vector<int> nums2(nums.begin() + 1, nums.end());  // 不抢第一间
        
        return max(getMaxRob(nums1), getMaxRob(nums2));  
    }


    int getMaxRob(vector<int>& nums) {
        int size = nums.size();
        if (size == 0) return 0;
        if (size == 1) return nums[0];
        
        // dp[i] represents the maximum amount of money we can rob up to house i
        vector<int> dp(size + 1, 0);
        
        dp[1] = nums[0];  // Robbing the first house
        
        // Start filling the dp array from the second house
        for (int i = 2; i <= size; ++i) {
            // dp[i] = max of not robbing this house (dp[i-1]) or robbing this house (dp[i-2] + nums[i-1])
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1]);
        }
        
        return dp[size];  // The maximum amount robbed is at dp[size]
    }
};
```
簡化
```c++

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];

        return max(robRange(nums, 0, n - 2), robRange(nums, 1, n - 1));
    }

private:
    int robRange(vector<int>& nums, int start, int end) {
        int prev2 = 0, prev1 = 0;
        for (int i = start; i <= end; ++i) {
            int curr = max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};

```
