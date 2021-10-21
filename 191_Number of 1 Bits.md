# Number of 1 Bits


## 原題目:
```
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.


Example 1:
    Input: n = 00000000000000000000000000001011
    Output: 3
    Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
    Input: n = 00000000000000000000000010000000
    Output: 1
    Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
    
Example 3:
    Input: n = 11111111111111111111111111111101
    Output: 31
    Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

```

## 思路 
每次確認最後一位是不是1,利用n & 1確認即可,之後再把n往又移1位

```c++

class Solution {
public:
    int hammingWeight(uint32_t n) {
          int count = 0; 
          while (n){  
            count += n & 1;    
            n >>= 1;
          }
          return count;
    }
};

```
## 思路 hammingWeight         
         
n      =  100110100
n - 1  =  100110011
n&(n-1)=  100110000

邏輯就是，n - 1 消除最後一個 1，同時把其後的 0 都變成 1，再和 n 做一次 & 運算，就可以僅僅把最後一個 1 變成 0 了。


```c++

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while(n > 0)
        {
            n &= (n-1);
            count++;
        }
        return count;
    }
};

```