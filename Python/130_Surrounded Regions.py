#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
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

# @lc code=end

