/*
 * @lc app=leetcode id=274 lang=csharp
 *
 * [274] H-Index
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution {
    public int HIndex(int[] citations) {        
        int max = int.MinValue;        
        Dictionary<int,int> count = new Dictionary<int, int>();

        foreach (int n in citations)
        {
            count[n] = count.ContainsKey(n) ? count[n] + 1 : 1;
            max = Math.Max(max,n);
        }        
        
        int prev = 0;
        for (int n = max; n > 0;n--){  
            count[n] = count.ContainsKey(n) ? count[n] + prev : prev;
            prev = count[n];
            if (count[n] >= n)
                return n;  
        }

        return 0;
    }
}
// @lc code=end

