# Move Zeroes


## 原題目:
```
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 
Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    
    
Example 2:
    Input: nums = [0]
    Output: [0]
 

Constraints:
    1 <= nums.length <= 10**4
    -2**31 <= nums[i] <= 2**31 - 1
```



## 思路
利用pointer紀錄位置,當值不為零,將pointer值修改並移動

```
  i
  p
  0 1 0 3 12
  ---------------
  p i  
  0 1 0 3 12 
  ----------------
    p i
  1 1 0 3 12
  ----------------
    p   i
  1 1 0 3 12
  ----------------
      p   i
  1 3 0 3 12
  ----------------
      p      i
  1 3 12 3 12 
```


#### C++

``` c++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int index = 0;
        for(auto n : nums){
           if(n != 0){
               nums[index++] = n;
           }
        }
        for(int i = index;i < nums.size();i++){
            nums[i] = 0;
        }
        
    }
};
``` 
