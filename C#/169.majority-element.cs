/*
 * @lc app=leetcode id=169 lang=csharp
 *
 * [169] Majority Element
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {
    public int MajorityElement(int[] nums) {
        int count = 0;
        int candidate = 0;
        foreach (int n in nums)
        {
            if (count == 0 ){
                candidate = n;
            }
            count += (n == candidate ? 1: -1);
        }
        return candidate;
    }

}
// @lc code=end

