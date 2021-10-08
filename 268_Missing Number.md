# Perfect Squares


## 原題目:
```
Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

Example 4:
    Input: nums = [0]
    Output: 1

Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.
 

Constraints:
    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique.
```

## 思路 set


#### C++

``` c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        set<int> numbers(nums.begin(),nums.end());
        for (int i = 0;i < nums.size();i++){            
            if(numbers.count(i) == 0 )
                return i;          
        }        
        return nums.size();         
    }
};    
``` 

## 思路 
假設nums = [3,0,1],需要比對[0,1,2,3],可以做xor 比對差異或是相減比較

``` c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0;i < nums.size();i++){            
            ans ^= nums[i];         
        }        
        for (int i = 0;i <= nums.size();i++){ 
            ans ^= i; 
        }        
        return ans;          
    }
};  
``` 


``` c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0;i <= nums.size();i++){ 
            ans += i; 
        }   
        for (int i = 0;i < nums.size();i++){            
            ans -= nums[i];         
        }        
     
        return ans;          
    }
};  
```

