# N-Queens

## 原題目:
```
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

    Input: 4
    Output: [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
```

## 思路1
backtracking 問題,每行只會擺放一個皇后,所以以raw 為單位放,不可能每次都整個迴圈判斷是否在攻擊範圍,這邊考慮以欄和對角線的判別<br>

以下介紹對角線如何判斷
```
對角/ ,將x +y 的值合起來判斷是否有重複

0  1  2  3
1  2  3  4
2  3  4  5
3  4  5  6
[False] * (2n - 1)


對角＼ ,可慮將x -y 的值合起來判斷

0  -1  -2  -3
1  0   -1  -2
2  1    0  -1
3  2    1   0
4  3    2   1

這邊因為値是負的,我們讓起始位置為0,加上n - 1

3  2  1  0
4  3  2  1
5  4  3  2
6  5  4  3
```



#### Python


## 思路2
 


#### Python
```python
class Solution:
 
    def solveNQueens(self, n):
        ans = []
        sol = [['.'] * n for _ in range(n)] 
        m = 2 * n - 1
        my,md1,md2 =[False] * n,[False] * m,[False] * m
        

        count = 0
        def backtracking(count,x):           
            if count == 0:                       
                ans.append([ ''.join(raw) for raw in sol ])         
                return                             
            for y in range(n):
                d1 = x + y
                d2 = x - y + (n - 1)
                if  not my[y] and not md1[d1] and not md2[d2]:                       
                    my[y],md1[d1],md2[d2] = True,True,True
                    sol[x][y] = "Q"                          
                    backtracking(count - 1,x + 1)
                    sol[x][y] = "."     
                    my[y],md1[d1],md2[d2] = False,False,False                   
                       

        backtracking(graph,n,0)
        return ans
```




