/*
 * @lc app=leetcode id=22 lang=csharp
 *
 * [22] Generate Parentheses
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        IList<string> ans = new List<string>();
        generateParenthesis(n,n,"",ans);
        return ans;
    }

    public void generateParenthesis(int l,int r,string s,IList<string> ans) {
        if ( l > r ){
            return ;
        }
        if (l == 0 && r == 0)
            ans.Add(s);   
        if (l > 0)     
            generateParenthesis(l - 1,r ,s + "(",ans);
        if (r > 0)
            generateParenthesis(l ,r - 1 ,s + ")",ans);            

    }

}
// @lc code=end

