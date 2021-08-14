class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not any(matrix):
            return 
        cols = set()
        rows = set()
        m,n = len(matrix),len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    cols.add(col)
                    rows.add(row)
        for row in range(m):
            for col in range(n):
                if col in cols or row in rows:
                    matrix[row][col] = 0