# Counting Bits


## 原題目:
```
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
    0 --> 0
    1 --> 1
    2 --> 10
    
Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
   0 <= n <= 105
```

##利用bit 的特性
n 的bit 1的個數是 n >> 1 再判斷尾數 

```
0 --> 000
1 --> 001
2 --> 100
3 --> 011
4 --> 100
5 --> 101
6 --> 110
```


#### C++
``` c++
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1,0);        
        for (int i = 1; i <= n ;i++ ){
            result[i] = result[i /2 ] + i%2;
            
        }
        return result;
    }
};
``` 



## 利用 n &(n - 1)
n 的bit 1的個數是n &(n - 1)bit 1的個數+1
#### C++

``` c++
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result(n + 1,0);        
        for (int i = 1; i <= n ;i++ ){
            result[i] = result[(i & i - 1)] + 1;
        }
        return result;
    }
};
``` 

















