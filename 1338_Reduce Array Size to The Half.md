# Jump Game III

## 原題目:
```
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:
    Input: arr = [3,3,3,3,5,5,5,2,2,7]
    Output: 2
    Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
    Possible sets of size 2 are {3,5},{3,2},{5,2}.
    Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

Example 2:
    Input: arr = [7,7,7,7,7,7]
    Output: 1
    
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
 

Constraints:
    2 <= arr.length <= 10**5
    arr.length is even.
    1 <= arr[i] <= 10**5
```

## 思路1

計算每個數字的個數,依照個數大到排序後,依依相加,當拿掉超過一半,回傳使用幾個數字


#### c++
``` c++
class Solution {
public:
    int minSetSize(vector<int>& arr) {
        int count = 0;
        int remove_count = 0;
        unordered_map<int,int> n_map ;
        for(auto n : arr){
            n_map[n]++;           
        }
        
        vector<int> numbers;
        for (auto x : n_map){
            numbers.push_back(x.second);
        }
        
        sort(numbers.begin(), numbers.end());
        
        for(int i = numbers.size()-1; i>=0; i--)
        {
            count += 1;
            remove_count += numbers[i];
            if(remove_count >= arr.size()/2)
                return count;
        } 
        return count;
    }     
    
};

```
using heapq

``` c++
class Solution {
public:   
    int minSetSize(vector<int>& arr) {
        unordered_map<int,int>umap;     
        
        for(auto n : arr){
            umap[n]++;           
        }
        priority_queue<int> pq;        
        for(auto it: umap) 
            pq.push(it.second);
        
        int ans = 0, minus = 0;
        while(!pq.empty())
        {
            ans++;
            minus += pq.top();            
            if(minus >= (arr.size()/2)) 
               return ans;
            pq.pop();
        }
        return ans;        
    } 
};

```

## 思路2

建立10^5的陣列,記錄每個數字的數量,在轉換成出現頻率有幾個數字,由頻率10^5依序往下,當出現頻率不是零,則計算次數+1,直到移除一半以上的數字


``` c++
class Solution {
public:   
    int minSetSize(vector<int>& arr) {
        int cnt[100001] = {0};
        for (auto v : arr)
            cnt[v]++;

        int freq[100001] = {0};

        //change to freq has number count
        for (int v = 1; v < 100001; v++) 
            if (cnt[v]) freq[cnt[v]]++;

        int ans = 0;
        int left = (arr.size()+1)>>1;

        for (int f = 100000; left > 0; f--){
            while (freq[f] && left > 0) {
                left -= f;
                freq[f]--;
                ans++;
            }
        }

        return ans;       
    }
    
    
    
};
```









