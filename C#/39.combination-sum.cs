/*
 * @lc app=leetcode id=39 lang=csharp
 *
 * [39] Combination Sum
 */

// @lc code=start
public class Solution {
    
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
        Dictionary<int, IList<IList<int>>> dp = new Dictionary<int, IList<IList<int>>>();         

        foreach (int candidate in candidates)
        {
            for (int j = candidate; j <= target; j++)
            {
                if (!dp.ContainsKey(j))
                    dp[j] = new List<IList<int>>();

                if (candidate == j)
                {   
                    dp[j].Add(new int[] { candidate }.ToList());        
                }
                if (dp.ContainsKey(j - candidate))
                {
                    foreach (List<int> q in dp[j - candidate])
                    {
                        var add = new List<int>(q);
                        add.Add(candidate);
                        dp[j].Add(add);
                    }
                }
            }
        }
        return dp.ContainsKey(target) ? dp[target] : new List<IList<int>>();
    }
    public IList<IList<int>> CombinationSum_backtracking(int[] candidates, int target) {
        IList<IList<int>> ans = new List<IList<int>>();
        backtracking(candidates,0,new List<int>(),target,ans);
        return ans;
    }

    public void backtracking(int[] candidates,int index,IList<int>path,int path_res,IList<IList<int>> ans){
        if (path_res < 0)
            return;        
        else if (path_res == 0){
            ans.Add(path);
            return;
        }
        
        for (int i = index; i < candidates.Length; i ++ )
        {
            path.Add(candidates[i]);
            backtracking(candidates,i,new List<int>(path),path_res - candidates[i],ans);
            path.RemoveAt(path.Count() - 1);
        }
        

    }
}
// @lc code=end

