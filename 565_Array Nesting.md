# Array Nesting

## 原題目:
```
You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k].
```

## 思路

類似dfs得概念

<a href = "https://leetcode.com/submissions/detail/548103748/">95%</a>
#### Python
``` python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        ans = 0
        for index in range(len(nums)):
            if not visited[index]:
                j,count = index,0                   
                while not visited[j]:
                    count += 1                    
                    visited[j] = True
                    j = nums[j] 
                ans = max(ans,count)               
        return ans
``` 



#### C#

<a href = "https://leetcode.com/submissions/detail/548103406/">100%</a>

```c_sharp
public class Solution {
    public int ArrayNesting(int[] nums) {
        int length = nums.Count();
        bool []visited = new bool[length];
        int res = 0;
        
        for(int i = 0;i<length;i++){
            if(!visited[i]){
                int j = i;
                int count = 0;
                
                while(!visited[j])
                {                    
                    count += 1;
                    visited[j] = true;
                    j = nums[j] ;
                }
                
                if(count >res)
                    res = count;
            }
            
        }
        
        
        
        return res;
        
    }
}
```
