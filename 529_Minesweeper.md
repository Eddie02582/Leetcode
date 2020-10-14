# Minesweeper


## 原題目:
```
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]


Example 2:

Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

```

## BFS



#### Python
``` python
from collections import deque


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        i,j = click
        if board[i][j] == 'M':
            board[i][j] ='X'
            return board
        
        queue = deque([click])
        visited = {}
        

        while queue:
            m = len(queue)
            for i in range(m):
                i,j = queue.popleft()     
                if  (i,j) not in visited:
                    visited[(i,j)] = True
                    number = self.check_number(board,i,j)
                    if number == 0:
                        board[i][j] = 'B'
                        ajcent = self.get_ajcent(board,i,j,visited)
                        if ajcent:
                            queue += ajcent  
                    else:
                        board[i][j] = str(number)                            
        
        return board
    
    def get_ajcent(self,board,i,j,visited):    
        max_i,max_j = len(board),len(board[0])        
        add_path = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        ajcents = []
        for d in add_path:        
            new_i,new_j = i + d[0],j + d[1]
            if 0 <= new_i < max_i and 0 <= new_j < max_j and board[new_i][new_j] == 'E' and (new_i,new_j) not in visited:                
                ajcents.append((new_i,new_j))
        return ajcents
    
    def check_number(self,board,i,j):
        number = 0
        max_i,max_j = len(board),len(board[0])        
        add_path = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        for d in add_path:
            new_i,new_j = i + d[0],j + d[1]
            if 0 <= new_i < max_i and 0 <= new_j < max_j and board[new_i][new_j] == 'M':
                number += 1        
        return number
``` 













