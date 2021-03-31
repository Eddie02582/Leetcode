/*
 * @lc app=leetcode id=258 lang=csharp
 *
 * [258] Add Digits
 */

// @lc code=start
using System.Linq;
using System;
public class Solution {
    public int AddDigits(int num) {     

        while (num > 9){
            char []arr = num.ToString().ToCharArray();   
            num = 0;         
            foreach (char c in arr)           
                num += c - '0';                 
        }           
        return num;              
    } 
    public int AddDigits__(int num) {        
        if (num < 10)
            return num;
        else
            return AddDigits(num.ToString().ToCharArray().Select(x => x -'0').Sum());            
    }    
}
// @lc code=end

