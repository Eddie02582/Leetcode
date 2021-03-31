/*
 * @lc app=leetcode id=275 lang=csharp
 *
 * [275] H-Index II
 */

// @lc code=start
using System;
public class Solution {
    public int HIndex(int[] citations) {  
        int count = 0;
        int ans = 0;
        for (int i = citations.Length - 1; i >= 0; i--)
        {
            if (citations[i] == 0)
                break;

            ans = count >= citations[i] ? Math.Max(ans, citations[i]) : Math.Max(ans, citations.Length - i);
            count += 1;

        }
        return ans;
    }
}
// @lc code=end

