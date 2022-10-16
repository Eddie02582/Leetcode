# Combinations

## 原題目:
```
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```



## 思路backtrack


#### Python
``` python
class Solution(object):
    def combine(self, n, k):
        def backtrack(path, start):
            if len(path) == k:
                res.append(path)
            for i in range(start, n+1):
                backtrack(path + [i], i + 1)
        
        res = []
        backtrack([], 1)
        return res 
```

#### c++
```c++
class Solution {
public:
    vector<vector<int>> combination;
    vector<vector<int>> combine(int n, int k) {         
        vector<int>path;
        backtracking(k,n,1,path);
        return combination;
    }  
    void backtracking(int k,int n,int curr,vector<int>&path){
        if(path.size() == k){
            combination.push_back(path);           
        }
        else if (curr <= n ){
            path.push_back(curr);
            backtracking(k,n,curr + 1,path);
            path.pop_back();
            backtracking(k,n,curr + 1,path);
        }        
    }
};
```

類似,比較快

```c++
class Solution {
public:
    vector<vector<int>> combination;
    vector<vector<int>> combine(int n, int k) {         
        vector<int>path;
        backtracking(k,n,1,path);
        return combination;
    } 
    void backtracking(int k,int n,int curr,vector<int>&path){
        if(path.size() == k){
            combination.push_back(path);           
        }
        for(int i = curr;i <= n;i++){
            path.push_back(i);
            backtracking(k,n,i + 1,path);
            path.pop_back();           
        }        
    }
    
};
```



## 思路
python 內建itertools



#### Python
``` python
class Solution(object):
    def combine(self, n: int, k: int) -> List[List[int]]:
        import itertools
        x = itertools.combinations(range(1,n + 1), k)
        return x
```







