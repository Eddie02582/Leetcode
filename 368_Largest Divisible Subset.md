# Largest Divisible Subset


## 原題目:
```
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 
Example 1:
    Input: nums = [1,2,3]
    Output: [1,2]
    Explanation: [1,3] is also accepted.
    
Example 2:
    Input: nums = [1,2,4,8]
    Output: [1,2,4,8]
```

## 思路backtracking(TLE)
先排序,每次都有選與不選的選擇,選的話就要現在選的與前一個選的是否整除
#### C++

``` c++
# include<vector>
# include<algorithm>

using namespace std;
class Solution {
public:
    vector<int> ans;
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        
        sort(nums.begin(), nums.end());
        vector<int> path;
        backtracking(nums,path,0);
        return ans;
    }

    void backtracking(vector<int>& nums,vector<int> &path,int loc){   
        if (loc > nums.size()){
            if(path.size() > ans.size()){              
                ans.assign(path.begin(),path.end() - 1);
            }            
            return;
        }   
        if(path.empty() ||nums[loc] % path[path.size() - 1] == 0){ 
            path.push_back(nums[loc]);
            backtracking(nums,path,loc + 1);
            path.pop_back();     
        }
        backtracking(nums,path,loc + 1);
       
    }  
};
``` 

## 思路dp
以[1,2,4,8,16,90],dp[i]表示選擇i最大的subset,此時dp[i]為dp[0]~dp[i-1]符合nums[i]除以最後一個元素整除的最大長度的vectort 加上nums[i]


i = 0,dp[0] =[1]
i = 1,dp[1] = [1,2]
i = 2,dp[2] = [1,2,4]
i = 3,dp[3] = [1,2,4,8]
i = 4,dp[4] = [1,2,4,816]
i = 5,dp[5] = [1,2,90]

``` c++
# include<vector>
# include<algorithm>

using namespace std;
class Solution {
public:
    vector<int> largestDivisibleSubset_dp(vector<int>& nums) {        
        int max_sub_loc = 0;
        vector<vector<int>> dp (nums.size(),vector<int>{});
        sort(nums.begin(), nums.end());

        for (int i = 0;i < nums.size();i++){
            int loc = -1,sub_size = -1;
            for (int j = 0;j < i; j++){
                int size = dp[j].size();    
                if( (size == 0 || nums[i] % dp[j][size - 1] == 0) && size > sub_size ){
                    loc = j;
                    sub_size = size;
                }                
            }
  
            if(loc >= 0)
                dp[i].assign(dp[loc].begin(),dp[loc].end());

            dp[i].push_back(nums[i]);

            if(dp[i].size() >dp[max_sub_loc].size()){
                max_sub_loc = i;               
            }

        }
      
        return dp[max_sub_loc];
    }


};


``` 


