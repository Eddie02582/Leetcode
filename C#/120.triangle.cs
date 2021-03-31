/*
 * @lc app=leetcode id=120 lang=csharp
 *
 * [120] Triangle
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution {

    public int MinimumTotal(IList<IList<int>> triangle) { 
        //down-top
        int m = triangle.Count();
        for (int row = m - 2;row >= 0;row--){
            for(int col = 0;col <triangle[row].Count();col ++){
                triangle[row][col] += Math.Min(triangle[row + 1][col],triangle[row + 1][col + 1]);
            }
        }
        return triangle[0][0];

    }
    public int MinimumTotal_TopDown(IList<IList<int>> triangle) {        
        //top-down
        int m = triangle.Count();
        for (int i = 1; i < m; i++)
        {
            for (int j = 0; j < triangle[i].Count(); j++)
            {
                if (j == 0)
                {
                    triangle[i][j] += triangle[i - 1][0];
                }
                else if (j == triangle[i - 1].Count())
                {
                    triangle[i][j] += triangle[i - 1][j - 1];
                }
                else
                {
                    triangle[i][j] = triangle[i][j] + Math.Min(triangle[i - 1][j - 1], triangle[i - 1][j]);
                }
            }

        }

        return triangle[m - 1].Min();
    }
}
// @lc code=end

