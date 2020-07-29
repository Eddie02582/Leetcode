# Subarray Product Less Than K


## 原題目:
```
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.
```

## 思路
動態規劃的題目,題目說落下最多col只能一動1<br>
```
轉移函數
値會等於原本的值加上從上一排j -1 ~ j + 1的最小値
A[i][j] = A[i][j] + min(A[i-1][j - 1],A[i-1][j],A[i-1][j + 1])

邊界當j = 0 ,此時j - 1超過index範圍
A[i][j] = A[i][j] + min(A[i-1][j],A[i-1][j + 1])

邊界當j = n - 1 此時j + 1超過index範圍
A[i][j] = A[i][j] +  min(A[i-1][j - 1],A[i-1][j],A[i-1][j + 1])
```

#### Python
``` python
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        for i in range(1,m):
            for j in range(0,n):
                if j == 0:
                    A[i][j] = A[i][j] + min(A[i-1][j],A[i-1][j + 1])
                elif j == n - 1:
                    A[i][j] = A[i][j] + min(A[i-1][j - 1],A[i-1][j])
                else:                    
                    A[i][j] = A[i][j] + min(A[i-1][j - 1],A[i-1][j],A[i-1][j + 1])
        
        return min(A[m - 1])
``` 












