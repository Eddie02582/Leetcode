# Permutations

## 原題目:
```
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

```


## 思路backtracking


#### Python

``` python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        def backtracking(array,visited):
            if len(array) == len(nums):
                res.append(array[:])
                return         
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    backtracking(array + [nums[i]],visited)
                    visited[i] = False

        visited = [False] * len(nums)        
        res = []
        backtracking([],visited)
        return res   
``` 
#### c++
```c++
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<bool>visited(nums.size(),false);
        vector<vector<int>> ans;
        vector<int> path;
        backtracking(nums,ans,path,visited);
        return ans;
        
    }

    void backtracking(const vector<int>& nums,vector<vector<int>> &ans,vector<int>& path,vector<bool>& visited){
        
        if(path.size() == nums.size()){
            ans.push_back(path);
            return ;
        }

        for(int i = 0;i<nums.size();i++)
        {
            if(!visited[i]){
                visited[i] = true;
                path.push_back(nums[i]);
                backtracking(nums,ans,path,visited);
                visited[i] = false;
                path.pop_back();
            }
        }
    }
};
```
利用swap 的方法
```c++
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    void permute(vector<vector<int>> &ans,int idx, vector<int> &arr){
        if(idx == arr.size()-1){
            ans.push_back(arr);
            return;
        }
        for (int i = idx; i < arr.size();i++){
            swap(arr[i], arr[idx]);
            permute(ans, idx + 1, arr);
            swap(arr[i], arr[idx]);
        }
    }
    vector<vector<int>> permute(vector<int>& arr) {
        vector<vector<int>> ans;
        permute(ans, 0, arr);
        return ans;
    }
};
```


## 思路2
1. num = 1,此時ans = [[]] => 對於每個ans插入不同的位置 =>temp[[1]]
2. num = 2 此時ans = [[1]] => 對於每個ans插入不同的位置 
    [1] => [1,2],[2,1] 
3. num = 3 此時ans = [[1]]=> 對於每個ans插入不同的位置 
    [1,2] => [3,1,2],[1,3,2],[1,2,3]
    [2,1] => [3,2,1],[2,3,1],[2,1,3]

####python

``` python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]
        for num in nums:
            temp = []
            for sub in ans:
                for i in range(len(sub) + 1):
                    temp.append(sub[0:i]+[num]+ sub[i:])
            ans = temp[:]

        return ans
``` 

遞迴版本
``` python
class Solution:
    def permute(self, nums: List[int],res = [[]]) -> List[List[int]]:    
        def permutation(nums,res):   
            if not nums:
                return res
            length = len(res)
            
            while length > 0:            
                sub = res.pop(0)            
                for j in range(len(sub) + 1): 
                    res.append(sub[0:j] + [nums[0]] + sub[j:])                 
                length -= 1        
            return permutation(nums[1:],res)
        return permutation(nums,[[]])
``` 

#### C++
```c++
#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    // []
    // [1]
    // [1,2],[2,1]
    // [3,1,2],[1,3,2],[1,2,3],[3,2,1],[2,3,1],[2,1,3]
    vector<vector<int>> permute(vector<int>& nums) {        
        vector<vector<int>> ans;
        ans.push_back(vector<int> {nums[0]});        

        for(int i = 1; i <nums.size();i++){
            int size = ans.size();
            vector<vector<int>> temp;
            for (int j = 0;j<size;j++){  
                for (int k = 0; k < ans[j].size() + 1;k++){
                    vector<int> sub (ans[j]);
                    sub.insert(sub.begin() + k,nums[i]);                    
                    temp.push_back(sub);                
                }
            };
            ans = temp;
        }
        return ans;        
    }
};
```

## 思路3

``` python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:        
        ans = []
        def permutation(nums,prefix):    
            if not nums:
                ans.append(prefix[::])
            else:
                for i in range(len(nums)):
                    rem = nums[0:i] + nums[i + 1:]
                    permutation(rem,prefix + [nums[i]])   
        permutation(nums,[])
        return ans
```
        
        
        
        
        
        
        
        
        
        
        
        
        
        