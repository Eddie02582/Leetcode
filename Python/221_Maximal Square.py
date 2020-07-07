class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int: 
        arr = [list(map(int, row)) for row in matrix]
        for i in range(1, len(arr)):
            for j in range(1, len(arr[i])):
                if arr[i][j] == 1:
                    arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
        return max([max(row) for row in arr], default=0) ** 2
        