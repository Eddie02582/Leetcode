# Gray Code


## 原題目:
```
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

    Input: 2
    Output: [0,1,3,2]
    Explanation:
    00 - 0
    01 - 1
    11 - 3
    10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1

Example 2:

    Input: 0
    Output: [0]
    Explanation: We define the gray code sequence to begin with 0.
                 A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
                 Therefore, for n = 0 the gray code sequence is [0].
    ```

## 思路backtracking
如果要列出所有可能使用


## Code

#### Python
```
這邊解釋一下
a: 101
b: 110
如果 a和b 差一位,表示a ^ b 一定是2的幕次
判斷2的幕次的方法c == (c & -c)


```


``` python
class Solution:
    def grayCode_(self, n):
        ans = []        
        visited = [False] * 2**n
        
        def backtracking(array):
            if len(array) == len(visited):
                ans.append(array[:])           
                return           
            for i in range(len(visited)):
                if not visited[i]:
                    if not array:
                        visited[i] = True
                        backtracking(array + [i]) 
                        visited[i] = False
                    else:
                        a = array[-1] ^ i     
                        b = a * -1                  
                        if  a == 1 or a == (a & b):  
                            visited[i] = True
                            backtracking(array + [i])                       
                            visited[i] = False


  
        backtracking([])   
        return ans  
```  

