# Maximal Square


## 原題目:
```
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

## 思路1 
定義 dp[i, j] 表示以i, j這格為右下角的時候，全部都是 1 的正方形最大邊長」<br>
那麼當 matrix[i][j] 是 "1" 的時候呢？我們注意到：假設答案是 k，那麼它的上方、左上方、左方都能夠畫出一個邊長是 k-1 的正方形！（因為只是少了一排而已啊）<br>

反之，如果 (i, j) 的上方、左上方、左方三個格子的數值最小值為 x，那麼以 (i, j) 為右下角的正方形邊長不得超過 x+1（那也只能是 x+1 了。）<br>
因此我們得到一個遞迴式：dp[i, j] = min(dp[i-1, j], dp[i, j-1], dp[i-1, j-1]) + 1<br>



#### Python
``` python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int: 
        arr = [list(map(int, row)) for row in matrix]
        for i in range(1, len(arr)):
            for j in range(1, len(arr[i])):
                if arr[i][j] == 1:
                    arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
        return max([max(row) for row in arr], default=0) ** 2
```  

```
class Solution:
    def maximalSquare(self, matrix):
        if not matrix :
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        side = 0
        
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
            side = max (side,matrix[0][j])
        
        for i in range(m):
            matrix[i][0] = int(matrix[i][0])
            side = max (side,matrix[i][0])

        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i][j - 1],matrix[i - 1][j],matrix[i - 1][j - 1]) + 1
                    side = max (side,matrix[i][j])  
        return side *side
```


#### C++


<a href = "https://leetcode.com/submissions/detail/594711133/">94%</a>

```c++
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> dp(m + 1,vector<int>(n + 1));
        int max_square = 0;
        for (int i = 0; i < m;i++){
            for (int j = 0;j < n;j++){ 
                if(matrix[i][j] == '1'){
                    if(i == 0 || j == 0)                    
                        dp[i][j] = 1;
                    else
                        dp[i][j] = min({dp[i][j - 1],dp[i - 1][j - 1],dp[i - 1][j]})  + 1;                    
                    max_square = max(max_square,dp[i][j]);
                }            
            }
        }
        return max_square * max_square;
    }
};
```




