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
        
        
        
        
sol = Solution()
input = [["E","E","E","E","E","E","E","E"],
["E","E","E","E","E","E","E","M"],
["E","E","M","E","E","E","E","E"],
["M","E","E","E","E","E","E","E"],
["E","E","E","E","E","E","E","E"],
["E","E","E","E","E","E","E","E"],
["E","E","E","E","E","E","E","E"],
["E","E","M","M","E","E","E","E"]]

Click = [0,0]
sol.updateBoard(input,Click)


     
        
        
        