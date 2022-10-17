# Rotate Array


## 原題目:
```
Given an array, rotate the array to the right by k steps, where k is non-negative. 
Example 1:

    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
    
    
Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation: 
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:
    1 <= nums.length <= 10**5
    -2**31 <= nums[i] <= 2**31 - 1
    0 <= k <= 105

```

## 思路 

nums[0]->temp[3]<br>
nums[1]->temp[4]<br>
nums[2]->temp[5]<br>
nums[3]->temp[6]<br>
nums[4]->temp[0]<br>
temp[(i + k)%k] = nums[i]

```c++

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int m = nums.size();
        k = k % m;
        vector<int>temps(m);
        for(int i = 0;i<m;i++){
            temps[(i + k)%m] = nums[i];
        }
        for(int i = 0;i<m;i++){
            nums[i] = temps[i];
        }     
    }
};

```
## 思路reverse

以切割點分別兩邊做reverse,最後再一起reverse,<a href = "https://leetcode.com/problems/rotate-array/discuss/1730142/JavaC%2B%2BPython-A-very-very-well-detailed-explanation">參考</a>
```
     [1,2,3,4|,5,6,7]
   =>[4,3,2,1|7,6,5] 
   =>[5,6,7,1,2,3,4] 
```
```c++
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int m = nums.size();      
        k = k % m;
        reverse(nums.begin(),nums.begin() + m -k);   
        reverse(nums.begin() + m -k,nums.end()); 
        reverse(nums.begin(),nums.end());     
    }
};

```