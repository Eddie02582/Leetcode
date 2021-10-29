#  Bitwise AND of Numbers Range


## 原題目:
```
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

    Input: [5,7]
    Output: 4
Example 2:

    Input: [0,1]
    Output: 0
```

## 思路1
迴圈作&運算,會TLE


#### Python

``` python
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int: 
        ans = m
        for i in range(m + 1, n + 1):  
            ans &= i        
        return ans  
``` 

## 思路2
依序比較從高位到低位,不相等回傳

``` python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        for i in range(31,-1,-1):  
            dm =  (left >> i)&1;
            dn =  (right >> i)&1;     
            if dm != dn:
                return ans
            elif dm and dn:
                ans += dm << i  
        
        return ans

```

```c++
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int ans = 0;
        for(int i = 31;i >=0;i--){
            int m = (left >> i)&1;
            int n = (right >> i)&1;            
            if(m != n){
                break;
            }
            ans += (m << i);             
        }
        return ans;
    }
};
```

## 思路3 

每次往右直到相等

```c++
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int cnt =0;
        
        while(left!=right)
        {
            right >>= 1;
            left >>= 1;
            cnt++;
        }
        
        return right << cnt;
    }
};
```