class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int: 
        arr = [list(map(int, row)) for row in matrix]
        for i in range(1, len(arr)):
            for j in range(1, len(arr[i])):
                if arr[i][j] == 1:
                    arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
        return max([max(row) for row in arr], default=0) ** 2

    def maximalSquare_(self, matrix):
        if not matrix :
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        side = 0
        
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
            side = max (side,matrix[0][j])
        
        for i in range(m):
            matrix[i][0] = int(matrix[i][0])
            side = max (side,matrix[i][0])

        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i][j - 1],matrix[i - 1][j],matrix[i - 1][j - 1]) + 1
                    side = max (side,matrix[i][j])  
        return side *side

    def maximalSquare_bfs(self, matrix: List[List[str]]) -> int:
        if not any(matrix):
            return 0
        m,n = len(matrix),len(matrix[0])
        from collections import deque
        max_squre = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    side = 0
                    queue = deque([(i,j)])
                    while queue:
                        side += 1
                        max_squre = max(max_squre,side)
                        length = len(queue)
                        for _ in range(len(queue)):
                            x,y = queue.popleft()
                            if any ( r < 0 or c < 0 or matrix[r][c] != "1" for (r,c) in [(x - 1,y),(x - 1,y - 1),( x , y - 1)]):
                                queue = []
                                break                          
                            queue.extend([(x - 1,y),(x-1,y - 1),(x,y - 1)])
             
                    
        return  max_squre * max_squre    