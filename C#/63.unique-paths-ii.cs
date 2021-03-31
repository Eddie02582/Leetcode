/*
 * @lc app=leetcode id=63 lang=csharp
 *
 * [63] Unique Paths II
 */

// @lc code=start

public class Solution {
    public int UniquePathsWithObstacles(int[][] obstacleGrid) {
        int row = obstacleGrid.Length;//row
        int col = obstacleGrid[0].Length;//col
        int[,] dp = new int[row, col];

        //for first col
        for (int i = 0; i < row; i++)
        {
            if (obstacleGrid[i][0] == 1)
                break;
            dp[i, 0] = 1;
        }

        //for first row
        for (int i = 0; i < col; i++)
        {
            if (obstacleGrid[0][i] == 1)
                break;
            dp[0,i] = 1;
        }


        for (int i = 1; i < row; i++)
        {
            for (int j = 1; j < col; j++)
            {
                if (obstacleGrid[i][j] == 1)
                    dp[i, j] = 0;
                else
                    dp[i, j] = dp[i, j - 1] + dp[i - 1, j];
            }
        }
        return dp[row - 1, col - 1];
    
    }

}
// @lc code=end


