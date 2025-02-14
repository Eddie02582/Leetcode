# Combination Sum II

## 原題目:
```
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

	Input: candidates = [10,1,2,7,6,1,5], target = 8
	Output: 
	[
	[1,1,6],
	[1,2,5],
	[1,7],
	[2,6]
	]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

```



## 思路backtracking

<ul>
	<li>1.排序： 由於數字串中有重複元素，首先需要對 candidates 進行排序，這樣可以更容易地處理重複的元素。</li>
	<li>2.回溯： 使用回溯算法來尋找所有的組合。每次嘗試從當前位置選擇一個數字，並向下遞歸。如果當前數字和前一個數字相同且前一個數字未被選擇過，則跳過當前數字以避免重複組合。</li>
	<li>3,停止條件： 當 target 小於零時，回溯過程應該停止，因為再選擇數字不可能達到目標。</li>

</ul>


#### Python

``` python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        def backtracking(arr,target,index = 0):
            if target == 0:
                ans.append(arr[:])
                return 
      
            
            for i in range(index,len(candidates)):
                if i > index and candidates[i] ==  candidates[i - 1]:
                    continue
                n = candidates[i]  
                
                # optimization: skip the rest of elements starting index
                if target - n <0:
                    break 
                
                backtracking(arr + [n],target - n , i + 1)

        ans = []        
        backtracking([],target)
        candidates.sort()     
        return ans
           
``` 

#### C++

```c++
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> current;
        
        // 排序數字，這樣可以更容易避免重複組合
        sort(candidates.begin(), candidates.end());
        
        // 開始回溯
        backtrack(candidates, target, 0, current, result);
        
        return result;
    }

private:
    // 回溯函數
    void backtrack(vector<int>& candidates, int target, int start, vector<int>& current, vector<vector<int>>& result) {
        if (target == 0) {
            // 當目標為0時，找到一個合法的組合
            result.push_back(current);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            // 如果當前數字與前一個數字相同，則跳過，避免重複組合
            if (i > start && candidates[i] == candidates[i - 1]) {
                continue;
            }

            // 如果當前數字大於目標，則無法繼續選擇該數字
            if (candidates[i] > target) {
                break;
            }

            // 選擇當前數字
            current.push_back(candidates[i]);
            // 進行遞歸
            backtrack(candidates, target - candidates[i], i + 1, current, result);
            // 回溯，撤回當前選擇
            current.pop_back();
        }
    }
};
```





