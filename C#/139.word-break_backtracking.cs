/*
 * @lc app=leetcode id=139 lang=csharp
 *
 * [139] Word Break
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {
    public bool WordBreak(string s, IList<string> wordDict) {
        bool is_ok =  backtracking("",s,wordDict) ;
        return is_ok;
    }

    public bool backtracking(string s,string match, IList<string> wordDict){
        if (s == match)
            
            return true;
        else if (s.Length >= match.Length)
            return false;

        int firstWoid = match[s.Length];
        for(int i = 0;i <wordDict.Count();i++){
            if (firstWoid == wordDict[i][0]){
                if (backtracking(s + wordDict[i],match,wordDict))
                    return true;
            }

        }


        return false;
    }
}
// @lc code=end

