# Surrounded Regions


## 原題目:
```
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
    Input: 
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    Explanation: 
        Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
        Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
        Two cells are connected if they are adjacent cells connected horizontally or vertically.


Example 2:
    Input: board = [["X"]]
    Output: [["X"]]

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.
    
```


## 思路BFS






## Code
可以判斷每個非邊界為O的做BFS,並且判斷這個區域是否包含邊界,不是就將O改成X,這邊反向思考利用邊緣作BFS將其區域找出改成*,剩下O即為被X包圍的區間,O改成X,將*改成O


``` python
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
       
        from collections import deque
        m,n = len(board),len(board[0])
      

        def bfs(r,c):
            queue = deque([(r,c)])          
            board[r][c] = "*"  
            while queue:
                r,c = queue.popleft()   
                for x,y in [(r +1,c),(r - 1,c),(r,c + 1),(r,c - 1)]:   
                    if 0 <= x < m and 0 <= y < n and board[x][y] == "O":  
                        board[x][y] = "*"   
                        queue.append((x,y))
   
        for r in range(m):
            for c in range(n): 
                if  (r == 0 or c == 0 or r == m - 1 or c == n - 1 ) and board[r][c] == "O":                     
                    bfs(r,c)

        for r in range(m):
            for c in range(n): 
                board[r][c] = "O" if board[r][c] == "*" else "X"  
        
``` 
 
優化
``` python
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
       
        from collections import deque
        m,n = len(board),len(board[0])
      

        def bfs(r,c):
            queue = deque([(r,c)])          
            board[r][c] = "*"  
            while queue:
                r,c = queue.popleft()   
                for x,y in [(r +1,c),(r - 1,c),(r,c + 1),(r,c - 1)]:   
                    if 0 <= x < m and 0 <= y < n and board[x][y] == "O":  
                        board[x][y] = "*"   
                        queue.append((x,y))
                        
        for i in range(m):
            space = range(n) if not i or i == m - 1 else (0, n - 1)
            for j in space:
                if board[i][j] == 'O': bfs(i, j)
                
        for r in range(m):
            for c in range(n): 
                board[r][c] = "O" if board[r][c] == "*" else "X"  
        
```  













