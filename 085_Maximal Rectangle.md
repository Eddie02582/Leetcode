# 85. Maximal Rectangle

## 原題目:
```
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

## 思路
將題目簡化成84題,建立dp計算出每個元素的高度,當dp[i][j] ==1,dp[i][j] = dp[i][j] +dp[i][j-1]高度 <br>
```
ex:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

dp = [
  [1,0,1,0,0],
  [2,0,2,1,1],
  [3,1,3,2,2],
  [4,0,0,3,0]
]

```
#### Python



``` python
class Solution:
    def maximalRectangle(self, matrix):
        area = 0
        dp = [ list(map(int,row)) for row in matrix]
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if dp[i][j] == 1:
                    dp[i][j] += dp[i- 1][j]
``` 



