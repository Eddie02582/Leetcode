class Solution:
    
    def get_options(self,board,row,col):
        options = set("123456789")
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