class Solution(object): 
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m,n = len(board),len(board[0])
        visited = [ [False] * n for _ in range(m)]          
        
        def backtracking(i,j,pos):  
            if pos == len(word):
                return True
            
            col_steps,row_steps = [1,-1,0,0],[0,0,1,-1]
            for col_step,row_step in zip(col_steps,row_steps):  
                col,row = j + col_step,row_step + i
                if 0 <= col < n and 0<= row < m and not visited[row][col] and board[row][col] == word[pos]:
                    visited[row][col] = True
                    if backtracking(row,col,pos + 1):
                        return True
                    visited[row][col] = False
                    
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    visited[row][col] = True
                    if backtracking(row,col,1):
                        return True
                    visited[row][col] = False
        
        return False
        
sol = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED" 
sol.exist(board,word)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE" 
sol.exist(board,word)

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB" 
sol.exist(board,word)
