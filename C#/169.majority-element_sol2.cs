/*
 * @lc app=leetcode id=169 lang=csharp
 *
 * [169] Majority Element
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int,int> times = new Dictionary<int, int>();
        foreach (int n in nums)
        {
            if (times.ContainsKey(n)){
                times[n] += 1;
            }
            else{
                times[n] = 1;
            }
            if (times[n] >= (nums.Length + 1)/2)
                return n;
        }
        return 0;

    }
}
// @lc code=end

