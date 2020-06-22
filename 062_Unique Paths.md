# Unique Paths

## 原題目:
```
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
    Input: m = 3, n = 2
    Output: 3
    Explanation:
    From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Right -> Down
    2. Right -> Down -> Right
    3. Down -> Right -> Right
    
Example 2:

    Input: m = 7, n = 3
    Output: 28
```

## 思路
除了第一列或是第一行只有一種走法,其餘每一個一定是從上方或左下方來,所以path(i,j) = path(i - 1,j) + path(i,j - 1)
```    
    path(i,j) = 1 , i == 0 or j == 0    
    path(i,j) = path(i - 1,j) + path(i,j - 1)    

```



#### Python
使用動態規劃
``` python
    def uniquePaths(self, m: int, n: int) -> int: 
        table = [[0] * m for _ in range(n)]   
        table[0][0] = 1
        
        for i in range(n):
            for j in range(m):        
                if i == 0 or j == 0:              
                    table[i][j] = 1
                else:                 
                    table[i][j] = table[i - 1][j] +table[i][j - 1]    
        return table[n - 1][m - 1] 
``` 

使用遞迴,這邊注意會timeout,所以使用一個字典記錄値,避免重複計算

``` python
from collections import defaultdict

routes = defaultdict(int)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 or n < 1:
            return 0
        elif m == 1 and n == 1:
            return 1
        elif (m, n) not in routes:
            routes[(m, n)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        return routes[(m, n)]

``` 

使用內嵌函數
``` python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:   
        visited = dict()
        def check_path(m,n):            
            if (m, n) in visited:
                return visited[(m, n)]  

            if m == 1 or n == 1:
                return 1                
            result = check_path(m - 1, n ) + check_path(m, n - 1)
            visited[(m, n)] = result           
            return result

        return check_path(m,n)

``` 

## 思路
(m -1)右與(n-1)左排列即是((m-1)+(n-1))!/((m-1)!*(n-1))!

``` python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:   
        def factorial(n):
            if n == 1:
                return n
            else:
                return n * factorial(n-1)
        
        if m == 1 or n == 1:
            return 1       
                
        return factorial(m + n - 2)/(factorial(m -1) * factorial(n - 1))

``` 






