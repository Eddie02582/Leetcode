# Remove Element

## 原題目:
```
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

    Given nums = [3,2,2,3], val = 3,

    Your function should return length = 2, with the first two elements of nums being 2.

    It doesn't matter what you leave beyond the returned length.
    
Example 2:

    Given nums = [0,1,2,2,3,0,4,2], val = 2,

    Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

    Note that the order of those five elements can be arbitrary.

    It doesn't matter what values are set beyond the returned length.
```

## 思路
用指針記錄,當前需要修改的位置,迴圈所有nums値,當指針不等於val,將値寫入

## Code

#### Python

```python
class Solution(object):
    def removeElement(self, nums, val):
        p = 0
        for x in nums:            
            if x != val:
                nums[p]=x
                p += 1 
        return p
        
```


<a href ="https://leetcode.com/submissions/detail/567287498/">100%</a>

#### C++

```c++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int index = 0;
        for (int i = 0;i < nums.size();i++)
        {
            if (nums[i] != val)
            {
                nums[index] = nums[i];
                index += 1;
            }
        }
        return index;
    }   
    
};








```


