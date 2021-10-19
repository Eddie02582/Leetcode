# Find All Duplicates in an Array


## 原題目:
```
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

    Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    Output: [-1,3,-1]
    Explanation: The next greater element for each value of nums1 is as follows:
    - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
    - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
    - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
    
Example 2:
    Input: nums1 = [2,4], nums2 = [1,2,3,4]
    Output: [3,-1]
    Explanation: The next greater element for each value of nums1 is as follows:
    - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
    - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:
    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 104
    All integers in nums1 and nums2 are unique.
    All the integers of nums1 also appear in nums2.
```

## 思路
題目的意思是nums1是nums2的以集合,並在nums2相對應的位置的下一個比他大的元素

#### c++

``` c++
#include <vector>
using namespace std;


class Solution {
public:
    //O(M*N)
    vector<int> nextGreaterElement_(vector<int>& nums1, vector<int>& nums2) {
        vector<int>ans(nums1.size() ,-1);
        for (int i = 0;i< nums1.size();i++){
            bool bfind = false;
            for (int j = 0;j < nums2.size();j++){
                if(nums1[i] == nums2[j])
                    bfind = true;   
                if(bfind && nums2[j] > nums1[i]){                   
                    ans[i] = nums2[j];
                    break;
                }

            }
        }
        
        return ans;
    }
};

``` 



## 思路利用stack 和map

先用map 記錄nums1數値與index對應的關係

這邊以[6,5,7,8,2]舉例堆疊
```
1.i = 0,n = 6,s = [6]
2.i = 1,n = 5,5比6小將元素放入,s = [6,5]
3.i = 2,n = 7,7大於5,將7記錄在剛剛map儲存的相對應的index,繼續比對=>s = []


```


``` c++
#include <vector>
#include <iostream>
#include <unordered_map>
#include <stack>
using namespace std;

class Solution {
public:  
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int>ans(nums1.size() ,-1);
        stack<int>s;
        unordered_map <int,int> loc;
        for (int i = 0;i< nums1.size();i++){
            loc[nums1[i]] = i;
        }       
        for (int j = 0;j < nums2.size();j++){
            while(!s.empty() && s.top() < nums2[j]){
                if(loc.count(s.top())){
                    ans[loc[s.top()]] = nums2[j];
                    s.pop();
                }
                else
                    break;                
            }  
            s.push(nums2[j]);
        }     
        return ans;
    }

};


``` 

