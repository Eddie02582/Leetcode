/*
 * @lc app=leetcode id=1 lang=csharp
 *
 * [1] Two Sum
 */

// @lc code=start

using System.Collections.Generic;
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> record = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++)
        {
            
            if (record.ContainsKey(target - nums[i])){

                return new int []{record[target - nums[i]],i};
                
            }
            record[nums[i]] = i;
        }
        
        return new int [] {0,0};
    }
}
// @lc code=end

