/*
 * @lc app=leetcode id=62 lang=csharp
 *
 * [62] Unique Paths
 */

// @lc code=start

public class Solution {
    public int UniquePaths(int m, int n) {
        if (m == 0 && n == 0)
            return 0;
        else if (m == 0 || n == 0)
            return 1;
        int[,] dp = new int[n, m];   
     
        for (int i = 0; i< n;i ++){
            for (int j = 0; j < m; j++)
            {
                if ( i == 0 || j == 0)
                    dp[i, j] = 1;            
                else
                    dp[i, j] = dp[i , j - 1] + dp[i - 1, j];
            }
        }
        return dp[n - 1, m - 1]; 
    }
    // dp 
    //   	1	2	3	4	5	6	7
    // 1	1	1	1	1	1	1	1
    // 2	1	2	3	4	5	6	4
    // 3	1	3	6	10	15	21	28    
}


// @lc code=end

