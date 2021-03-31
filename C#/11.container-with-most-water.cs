/*
 * @lc app=leetcode id=11 lang=csharp
 *
 * [11] Container With Most Water
 */

// @lc code=start
using System;
public class Solution {
    public int MaxArea(int[] height) {        
        int maxArea = 0 ;        
        int left = 0;
        int right = height.Length - 1;
        while (left < right){
            maxArea = Math.Max((right - left) * Math.Min(height[left],height[right]),maxArea);          
            if (height[left] < height[right])                          
                left += 1;   
            else              
                right -= 1;                
        }
        return maxArea;
        
    }
}
// @lc code=end

