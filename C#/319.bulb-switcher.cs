/*
 * @lc app=leetcode id=319 lang=csharp
 *
 * [319] Bulb Switcher
 */

// @lc code=start

public class Solution {
    public int BulbSwitch(int n) {
        //assume 0 is open 
        if (n <= 1)
            return n;           
        int[] light = new int[n];
        for (int i = 2; i <= n; i++)
        {
            if (i == 2)
            {
                for (int j = i; j <= n; j += i)
                {
                    light[j - 1] = 1;
                }
            }
            else
            {
                for (int j = i; j <= n; j += i)
                {
                    light[j - 1] = light[j - 1] == 1 ? 0 : 1;
                }
            }

        }
        int ans = 0;
        foreach (int item in light)
        {
            if (item == 0)
                ans += 1;
        }
        return ans;
        
    }
}
// @lc code=end

