# Complement of Base 10 Integer


## 原題目:
```
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

 

Example 1:
    Input: n = 5
    Output: 2
    Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
    
Example 2:
    Input: n = 7
    Output: 0
    Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

Example 3:
    Input: n = 10
    Output: 5
    Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Constraints:

0 <= n < 109


```

## 思路
從低位到高位一個取出,並將値取反,並將値轉成十進位返回(取出的値移到原本的位置)
利用n&1取出最後一位,並使用^1,將1->0,0->1

1. n = 5(101),res = 0, (5 & 1)^1 = 0 =>res = 0
2. n = 2 (10),res = 2, (2 & 1)^1 = 1 =>res = res + (1<<1)
3. n = 2 (1),res = 2, (1 & 1)^1 = 0 =>res = res + (0<<2)


#### C++
``` c++
class Solution {
public:
    int bitwiseComplement(int n) {
        if (n==0)
            return 1;
        int i = 0,res = 0;        
        while (n){
            res += ((n & 1)^1) << i;
            n >>= 1;
            i += 1;           
        }       
        return res;   
    }
};
``` 

## 思路利用補碼
5為2進制為101,只要對111做xor 即可得到010

#### C++
``` c++
class Solution {
public:
    int bitwiseComplement(int n) {
        if (n==0)
            return 1;
        int temp = n;
        int t = 0;
        while (temp){
            temp = temp >> 1;
            t = (t << 1 )+ 1;
        }       
        return t^n;   
    }
};
``` 

簡化
``` c++
class Solution {
public:
    int bitwiseComplement(int n) {
        if (n==0)
            return 1;
      
        int t = 1;
        while (n > 1){           
            t = (t << 1 )+ 1;          
        }       
        return t^n;   
    }
};
``` 











