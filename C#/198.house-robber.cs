/*
 * @lc app=leetcode id=198 lang=csharp
 *
 * [198] House Robber
 */

// @lc code=start
using System;
public class Solution {
    public int Rob(int[] nums) {  
        int prev_two = 0;
        int prev_one = nums[0];
        for (int i = 1;i < nums.Length; i ++){           
            nums[i] = Math.Max(prev_one,prev_two + nums[i]);
            prev_two = prev_one;
            prev_one = nums[i];                     

        }
        return prev_one;
    }
}
// @lc code=end

