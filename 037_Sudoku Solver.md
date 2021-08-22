# Sudoku Solver

## 原題目:
```
Write a program to solve a Sudoku puzzle by filling the empty cells.

	A sudoku solution must satisfy all of the following rules:

	Each of the digits 1-9 must occur exactly once in each row.
	Each of the digits 1-9 must occur exactly once in each column.
	Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
	The '.' character indicates empty cells.

Input: board = 
[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]
Output: 
[["5","3","4","6","7","8","9","1","2"],
 ["6","7","2","1","9","5","3","4","8"],
 ["1","9","8","3","4","2","5","6","7"],
 ["8","5","9","7","6","1","4","2","3"],
 ["4","2","6","8","5","3","7","9","1"],
 ["7","1","3","9","2","4","8","5","6"],
 ["9","6","1","5","3","7","2","8","4"],
 ["2","8","7","4","1","9","6","3","5"],
 ["3","4","5","2","8","6","1","7","9"]
 ]

```



## 思路backtracking

找出每次的選擇做backtracking
#### Python


``` python
class Solution:
    
    def get_options(self,board,row,col):
        options = set(["1","2","3","4","5","6","7","8","9"])
        exist = set()        
        for i in range(9):
            if board[i][col] != ".":
                exist.add(board[i][col])
        for j in range(9):
            if board[row][j] != ".":
                exist.add(board[row][j])
        
        start_row = 3 * (row //3)
        start_col = 3 * (col //3)
        
        for i in range(start_row,start_row + 3):
            for j in range(start_col,start_col + 3):
                if board[i][j] != ".":
                    exist.add(board[i][j])
        
        return options - exist              
    
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = [(i,j) for i in range(9) for j in range(9) if board[i][j] == '.']
        
        
        def backtracking(board,loc):
            if loc == len(queue):
                return True
            
            row,col = queue[loc] 
            for option in self.get_options(board,row,col):
                board[row][col] = option
                if backtracking(board,loc + 1):
                    return True
                board[row][col] = "."
        
        
        
        backtracking(board,0)
          
           
``` 

簡化(沒比較快)


```python
class Solution:
    
    def get_options(self,board,row,col):
        options = set("123456789")
        
        s1 = board[row]
        s2 = [board[i][col] for i in range(9)]
        
        start_row = 3 * (row //3)
        start_col = 3 * (col //3)        
        s3 = [ board[i][j] for i in range(start_row,start_row + 3) for j in range(start_col,start_col + 3)]  
        return options - set(s1 + s2 + s3)        
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = [(i,j) for i in range(9) for j in range(9) if board[i][j] == '.']
        
        
        def backtracking(board,loc):
            if loc == len(queue):
                return True            
            row,col = queue[loc] 
            for option in self.get_options(board,row,col):
                board[row][col] = option
                if backtracking(board,loc + 1):
                    return True
                board[row][col] = "."        
        backtracking(board,0)
```


每次填入數字判斷backtracking
#### Python


``` python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrow, ncol = len(board), len(board[0])
        empty = []
        
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == ".":
                    empty.append([i, j])
        
        all_nums = set([str(i) for i in range(1, 10)])
        
        def getChoices(coord):
            x, y = coord
            s1 = board[x]
            s2 = [board[i][y] for i in range(ncol)]
            s3 = []
            startx = x // 3 * 3      
            starty = y // 3 * 3
            
            for i in range(startx, startx+3):
                for j in range(starty, starty+3):
                    s3.append(board[i][j])
            s = set(s1 + s2 + s3)
            return list(all_nums - s)
            
        def helper(idx = 0):
            if idx == len(empty):                
                return True
            x, y = empty[idx]
            possibilities = getChoices((x, y))
            for num in possibilities:
                board[x][y] = num
                if helper(idx + 1):
                    return True
                board[x][y] = "."
            return False     
        
        helper(idx = 0)
        
        return board  
```







