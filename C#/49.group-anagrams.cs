/*
 * @lc app=leetcode id=49 lang=csharp
 *
 * [49] Group Anagrams
 */

// @lc code=start
using System.Collections.Generic;
public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, IList<string>> group = new Dictionary<string, IList<string>>();
     
        IList<IList<string>> ans = new List<IList<string>>();

        foreach (string s in strs)
        {
            char[] array = s.ToCharArray();
            Array.Sort(array);
            string key = new string(array);
            if (group.ContainsKey(key))
                group[key].Add(s);
            else
            {  
                group[key] = new List<string>();
                group[key].Add(s);
            }
        }
        foreach (IList<string> data in group.Values)    
            ans.Add(data);   

        return ans;

    }
}
// @lc code=end







