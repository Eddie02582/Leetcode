# House Robber


## 原題目:
```
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.
    
Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12. 

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
```

## 思路 dp
計錄當下最佳選擇,以[2,7,9,3,1]為例,<br>
1.[2],只能選[2]<br>
2.[2,7],選擇max([2,7])<br>
3.[2,7,9],從3之後就有2種情況,第一種是前項,第二種是選擇前前項並加上現在這項,即dp[i] = max(dp[i - 1],dp[i - 2] + dp[i])<br>


#### C#

```csharp
using System;
public class Solution {
    public int Rob(int[] nums) {  
        int prev_two = 0;
        int prev_one = nums[0];
        for (int i = 1;i < nums.Length; i ++){           
            nums[i] = Math.Max(prev_one,prev_two + nums[i]);
            prev_two = prev_one;
            prev_one = nums[i];                     

        }
        return prev_one;
    }
}
```

#### C++

```c++

#include <iostream>
#include <vector> 
using namespace std;

class Solution {
public:
    int rob_(vector<int>& nums) {
        int size = nums.size();        
        vector<int> dp(size + 1, 0);
         dp[1] = nums[0];
        for (int i = 2;i <= size; i ++){            
            dp[i] = max(dp[i - 1],dp[i - 2] + nums[i - 1]);
        }        
        return dp[size];
    }
};

```
簡化只需要儲存前一項和前前項

```c++
// Your First C++ Program

#include <iostream>
#include <vector> 
using namespace std;

class Solution {
public:
    int rob_(vector<int>& nums) {
        int size = nums.size();        
        vector<int> dp(size + 1, 0);
         dp[1] = nums[0];
        for (int i = 2;i <= size; i ++){            
            dp[i] = max(dp[i - 1],dp[i - 2] + nums[i - 1]);
        }        
        return dp[size];
    }

    int rob_simple(vector<int>& nums) {
        int prev_two = 0;
        int prev_one = nums[0];
      
        for (int i = 1;i < nums.size(); i ++){  
            int current = max(prev_one,prev_two +  nums[i]);  
            prev_two = prev_one;     
            prev_one = current;            
           
        }        
        return prev_one;
    }


};

```
