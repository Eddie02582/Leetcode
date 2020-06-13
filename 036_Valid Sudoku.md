# Valid Sudoku

## 原題目:
```
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.



```
題目的意思判斷數獨是否可以解


## 思路
主要分三部分,row,col,3x3,每個情況內數字不可重複

``` python
class Solution:
    def isValidSudoku(self, board):
        def isSafe(x,y):            
            for col in range(9):
                if y != col and board[x][y] == board[x][col]:                    
                    return False
            for row in range(9):
                if x != row and board[x][y] == board[row][y]:            
                    return False           
            start_row = 3*(x//3)
            start_col = 3*(y//3)
     
            for row in range(start_row,start_row + 3):
                for col in range(start_col,start_col + 3):
                    if col != y and row != x and board[x][y] == board[row][col]:                    
                        return False
            return True
                    
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    if not isSafe(row,col):
                        return False        
    
        return True

``` 

## 思路1
主要分三部分,row,col,3x3,每個情況內數字不可重複,利用set來判斷,是否値重複




#### Python

``` python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
     
        
        for row in range(9):
            exist = set()
            for col in range(9):
                n = board[row][col]
                if n != "." and n in exist:
                    return False
                exist.add(n)
       
        for col in range(9):
            exist = set()
            for row in range(9):
                n = board[row][col]
                if n != "." and n in exist:
                    return False
                exist.add(n)

        
        for colstart in range(0,9,3):            
            for rowStart in range(0,9,3): 
                exist = set()     
                for row in range(rowStart,rowStart + 3):                
                    for col in range(colstart,colstart + 3):
                        n = board[row][col]
                        if n != "." and n in exist:
                            return False
                        exist.add(n)        
        return True
           
``` 
