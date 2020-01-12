class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        colChoicesToEqRows = defaultdict(int)
        for row in matrix:
            zeroCols = [str(i) for i, val in enumerate(row) if val == 0]
            oneCols = [str(i) for i, val in enumerate(row) if val == 1]
            colChoicesToEqRows[''.join(zeroCols)] += 1
            colChoicesToEqRows[''.join(oneCols)] += 1
           
        return max(rows for rows in colChoicesToEqRows.values())
        
        
solution = Solution()

assert solution.maxEqualRowsAfterFlips([[0,1],[1,1]]) == 1

assert solution.maxEqualRowsAfterFlips([[0,1],[1,0]]) == 2

assert solution.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]) == 2


array = [[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,1,1,0,1,1,1,0,1,1,1]]

assert solution.maxEqualRowsAfterFlips(array) ==2
#assert solution.maxEqualRowsAfterFlips([[0,0,0],[0,1,1],[1,1,0]]) ==1 


