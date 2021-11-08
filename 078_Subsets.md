# Subsets

## 原題目:
```
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
```

參考
<a href = "https://leetcode.com/problems/subsets/solution/">Solution</a>

## 思路Cascading
在每一層output 再加上這層的選擇<br>

1. []<br>
2. output = [],choice = [1] => new_output = [],[1]<br>
3. output = [],[1],choice = [2] => new_output = [],[1],[2],[1,2]<br>
4. output = [],[1],[2],[1,2],choice = [3] => new_output = [],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]<br>
->[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#### Python
``` python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = [[]]
        
        for num in nums:
            temp = []
            for curr in output:
                temp.append(curr + [num])  
            output += temp
        return output
```
#### C++
```c++
#include<vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        ans.push_back(vector<int>{});

        for (int n:nums ){
            vector<vector<int>> subs = ans;           
            for (vector<int> sub :subs ){
                sub.push_back(n);
                ans.push_back(sub);
            }
            
        }
        return ans;

    }
};
```





## 思路backtrack

0:[]
1:[1],[2],[3]
2:[1,2],[1,3],[2,3]
3:[1,2,3]


->[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

#### Python

這個思路是選0個到選n個
``` python
class Solution(object):
    def subsets(self, nums):      
        def backtrack(first = 0, curr = []):           
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):               
                curr.append(nums[i])               
                backtrack(i + 1, curr)               
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()  
        return output

```

#### C++
```c++
class Solution {
public:   

    vector<vector<int>> subset_ans;
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;
        for (int i = 0;i<=nums.size();i++){
            helper(nums,path,0,i);        
        }
        return subset_ans;

    }
    void helper(vector<int>& nums,vector<int>& path,int start,int n){       
        if(path.size() == n)
        {
            subset_ans.push_back(path);
            return ;
        }
        if(start == nums.size()){
            return;
        }        
        path.push_back(nums[start]);
        helper(nums,path,start + 1,n);
        path.pop_back();
        helper(nums,path,start + 1,n);

    }

};
```


## 思路backtrack 2

backtrack 的思路,每次都有選與不選的選擇

                
```            
1          []                  [1]
          /   \             /       \    
2        []   [2]        [1]       [1,2]
        / \   / \        / \       /    \
3     [] [3][2] [2,3]  [1] [1,3] [1,2] [1,2,3]

->[],[3],[2],[2,3],[1],[1,3],[1,2],[1,2,3]
```   

#### Python
``` python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        if not nums:
            return []
        
        ans = []
        def backtracking(s,sol):
            if s == len(nums):
                ans.append(sol[:])
                return 
            backtracking(s + 1,sol)
            backtracking(s + 1,sol + [nums[s]]) 
        backtracking(0,[])        
        return ans

```
#### C++
```
#include<vector>
using namespace std;

class Solution {
public:  

    vector<vector<int>> subset_ans;

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> path;       
        helper(nums,path,0);     
        return subset_ans;

    }

    void helper(vector<int>& nums,vector<int>& path,int start){              
        if(start == nums.size()){
            subset_ans.push_back(path);
            return;
        }  
            
        path.push_back(nums[start]);
        helper(nums,path,start + 1);
        path.pop_back();
        helper(nums,path,start + 1);  

    }

};
```



## 思路dfs
```

                []
          /      |      \
         /       |       \          
       [1]      [2]      [3]        
      /  \       |
   [1,2] [1,3]  [2,3]
    |
   [1,2,3]

->[],[1],[1,2],[1,2,3],[2],[2,3],[3]
```                  


``` python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        if not nums:
            return []
        
        ans = []
        def dfs(s,sol):            
            ans.append(sol[:])            
            for i in range(s,len(nums)):                
                dfs(i + 1,sol + [nums[i]])  
        dfs(0,[])        
        return ans
```

## 思路bitmask


#### Python
``` python
class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output  
```







