# Two Sum


## 原題目:
```
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

```

## 思路

建立一個map字典,用來紀錄數值和陣列的位置,遍歷所有數字若target-數字在字典,回傳index



Python

``` python
class Solution:
    def twoSum(self, nums, target):
        map = {}
        for index,n in enumerate(nums):
            map[n] = index
            
        for index,n in enumerate(nums):
            if target-n in map:
                return [index,map[target-n]]   
        return []
```  

進階
``` python
class Solution:
    def twoSum(self, nums, target):
        map={}
        for index,n in enumerate(nums):
            if target-n in map:
                return [map[target-n],index]            
            map[n]=index        
        return []
```  


c++

<a href = "https://leetcode.com/submissions/detail/567071106/">95%</a>

```c++
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> lookup;   
        for (int i = 0; i < nums.size(); i++)
        {
            int n = target - nums[i];
            if (lookup.find(n) != lookup.end()) 
                return { lookup[n], i};
            lookup[nums[i]] = i;        
        }
        return {};          
    }  

};






```












