# Path Sum III


## 原題目:

```
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
```

<img src = "https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg">
```
    Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    Output: 3
    Explanation: The paths that sum to 8 are shown.
```

## 思路Backtracking + DP
```
      10
     /  \ 
    5    -3
   /  \    \ 
  3    2    11
 / \    \
3  -2   1
```
記錄路徑,每次把前面路徑加上當前節點的值,若合等於targetSum,次數+1,最後增加當前節點
ex:
```
 10   ->5      ->3     ->3
[10] [15,5]  [18,8,3] [18,8,3,3]

10    ->5     ->3      ->-2
[10] [15,5] [18,8,3] [21,11,6,3]

10     ->5    ->2      ->1
[10] [15,5]  [17,7,2]  [18,8,3]

10    -> -3  -> 11
[10]  [7,-3]  [18,8,11]
```


#### c++

``` python
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int count = 0;
    int pathSum(TreeNode* root, int targetSum) {
        vector<long> sums;
        dfs(root,sums, targetSum);
        return count;
    }
    void dfs(TreeNode* root,vector<long> sums, int targetSum){
        if (!root)
            return;       
        
        if(root->val == targetSum)
             count += 1;
        for (int i = 0;i < sums.size();i++){   
            sums[i] += root->val;
            if (sums[i] == targetSum)
                count += 1;                  
        }       
        sums.push_back(root->val);
        if(root->left){
            dfs(root->left,sums, targetSum);
        }
        if(root->right){
            dfs(root->right,sums, targetSum);  
        }   
        sums.pop_back();
        for (int i = 0;i < sums.size();i++){     
            sums[i] -= root->val;
        }
    }
};

       
``` 








