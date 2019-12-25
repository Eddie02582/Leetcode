class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #1.row
        
        for row in range(9):
            count = {}
            for col in range(9):
                n = board[row][col]
                if n != "." and n in count:
                    return False
                count[n] = 1
        #col
        for col in range(9):
            count = {}
            for row in range(9):
                n = board[row][col]
                if n != "." and n in count:
                    return False
                count[n] = 1

        
        for colstart in range(0,9,3):            
            for rowStart in range(0,9,3): 
                count = {}           
                for row in range(rowStart,rowStart + 3):                
                    for col in range(colstart,colstart + 3):
                        n = board[row][col]
                        if n != "." and n in count:
                            return False
                        count[n] = 1    
                print ('------------')   
        return True
        
        
arr = [[".",".",".",".","5",".",".","1","."],
       [".","4",".","3",".",".",".",".","."],
       [".",".",".",".",".","3",".",".","1"],
       ["8",".",".",".",".",".",".","2","."],
       [".",".","2",".","7",".",".",".","."],
       [".","1","5",".",".",".",".",".","."],
       [".",".",".",".",".","2",".",".","."],
       [".","2",".","9",".",".",".",".","."],
       [".",".","4",".",".",".",".",".","."]
     ]

sol = Solution()
sol.isValidSudoku(arr)