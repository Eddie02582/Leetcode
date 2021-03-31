/*
 * @lc app=leetcode id=7 lang=csharp
 *
 * [7] Reverse Integer
 */

// @lc code=start
public class Solution {
    public int Reverse(int x) {
        int flag =  x  < 0 ?  -1 :1 ;
        long  reverse = 0;
        x = x * flag;

        while (x != 0){

            reverse = reverse * 10 + x % 10;
            x = x /10;
        } 

        return  (reverse <= int.MaxValue && reverse >= int.MinValue) ? (int)(reverse * flag): 0;
    }
}
// @lc code=end

