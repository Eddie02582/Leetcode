/*
 * @lc app=leetcode id=139 lang=csharp
 *
 * [139] Word Break
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {

    //apple
    public bool WordBreak(string s, IList<string> wordDict) {
        int length = s.Length;
        bool[] dp = new bool[length + 1];
        dp[0] = true;

        for (int i = 1; i < dp.Length; i++)
        {
            for (int j = 0;j < i;j++ )
            {
                string word = s.Substring(j, i - j);
                if (dp[j] && wordDict.Contains(word))
                    dp[i] = true;
            }
        }

        return dp[length];
    }
    //timeout
    public bool WordBreak_BFS(string s, IList<string> wordDict) {
        List<string> queue = new List<string>();
        queue.Add("");        
        while(queue.Count() != 0)
        {
            string match = queue[0];
            queue.RemoveAt(0);
            for(int i = 0;i <wordDict.Count();i++){                
                int length = match.Length + wordDict[i].Length;
                string word = match +wordDict[i];
                if (word == s)
                    return true;             

                else if (word.Length < s.Length && word == s.Substring(0, length))
                {
                    queue.Add(match + wordDict[i]);
                }                       
            }
            

        }          
        return false;
    }

}
// @lc code=end

