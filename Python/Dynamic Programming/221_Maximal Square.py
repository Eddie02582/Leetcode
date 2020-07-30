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
        