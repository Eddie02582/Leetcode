/*
 * @lc app=leetcode id=3 lang=csharp
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
using System;
using System.Collections.Generic;
public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int left = 0;
        int right = 0;
        int ans = 0 ;
        HashSet<int> exist = new HashSet<int>();

        while(right < s.Length){   

            while (exist.Contains(s[right])){
                exist.Remove(s[left]);
                left += 1;
            } 
            exist.Add(s[right]);                   
            ans = Math.Max(right - left + 1,ans);
            right += 1;  
        }

        return ans;
    }
}
// @lc code=end

