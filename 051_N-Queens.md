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
backtracking 問題,每一格都有「放」和「不放」兩種選擇，放的時候要注意是否在攻擊範圍


#### Python

``` python
class Solution:
    def solveNQueens(self, n) : 
        m = 2*n - 1
        mx,my,md1,md2 = [False] * n,[False] * n,[False] * m,[False] * m
        sol = [[""]*n for i in range(n)]
        res = []
        def backtracking(x,y,c):
            if y == n:
                x += 1
                y = 0        
            if x == n:
                if c == n:                    
                    res.append( [ ".".join(row) for row in sol])
                return
            
            d1 = (x + y) % m
            d2 = (x - y + m) %m
            
            if not mx[x] and not my[y] and not md1[d1] and not md2[d2]:
                mx[x],my[y],md1[d1],md2[d2] = True,True,True,True
                sol[x][y] = "Q"
                backtracking(x,y + 1,c + 1)
                mx[x],my[y],md1[d1],md2[d2] = False,False,False,False
            
            sol[x][y] = ""
            backtracking(x,y + 1,c)

        backtracking(0,0,0)
        return res 
``` 

## 思路2
 
簡化上面,可以確定每行只會擺放一個皇后,線為單位來遞迴窮舉

#### Python
```python
class Solution(object):
    def solveNQueens(self, n: int) -> List[List[str]]:        
        m = 2*n - 1
        my,md1,md2 =[False] * n,[False] * m,[False] * m
        sol = [[""]*n for i in range(n)]
        res = []
        def backtracking(x):     
            if x == n: 
                res.append( [ ".".join(row) for row in sol])
                return
            
            for y in range(n):   
                d1 = (x + y) % m
                d2 = (x - y + m) %m            
                if not my[y] and not md1[d1] and not md2[d2]:
                    my[y],md1[d1],md2[d2] = True,True,True
                    sol[x][y] = "Q"
                    backtracking(x + 1)
                    my[y],md1[d1],md2[d2] = False,False,False            
                    sol[x][y] = ""
                

        backtracking(0)
        return res
```




