# Find Original Array From Doubled Array

## 原題目:
```
An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, 

and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.


Example 1:
    Input: changed = [1,3,4,2,6,8]
    Output: [1,3,4]
    Explanation: One possible original array could be [1,3,4]:
    - Twice the value of 1 is 1 * 2 = 2.
    - Twice the value of 3 is 3 * 2 = 6.
    - Twice the value of 4 is 4 * 2 = 8.
    Other original arrays could be [4,3,1] or [3,1,4].    
    
Example 2:
    Input: changed = [6,3,0,1]
    Output: []
    Explanation: changed is not a doubled array.
    
Example 3:
    Input: changed = [1]
    Output: []
    Explanation: changed is not a doubled array.
 

Constraints:
    1 <= changed.length <= 10**5
    0 <= changed[i] <= 10**5

```



## 思路 

先排序,然後由小開始配對,如果配對到就移除,如果沒配對到就回傳空陣列,利用map記綠每個數字的各數,配對完即移除各數


#### c++


```c++
class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        sort(changed.begin(),changed.end());
        unordered_map<int,int> counts;
        vector<int> ans ;
        for(auto n : changed){
            counts[n]++;
        }
        
        for(auto n : changed){
            if(counts[n] > 0){                   
                counts[n]--;
                counts[2 * n] --;
                ans.push_back(n);
                if(counts[2 * n] < 0)
                    return vector<int>{};
                
            }        
        }        
        return ans;    
    }
};

```