/*
 * @lc app=leetcode id=22 lang=csharp
 *
 * [22] Generate Parentheses
 */

// @lc code=start
using System.Collections.Generic;

class Queue{
        public string s = "";
        public int l  = 0;
        public int r = 0;
}

public class Solution {

    public IList<string> GenerateParenthesis(int n)
    {
        IList<string> ans = new List<string>();
        List<Queue> queues = new List<Queue>();
        queues.Add(new Queue { l = n, r = n, s = "" });
        while (queues.Count()> 0)
        {
            Queue queue = queues[0];
            queues.RemoveAt(0);
            if (queue.l == 0 && queue.r == 0)
                ans.Add(queue.s);
            if (queue.l <= queue.r)
            {
                if (queue.l > 0)              
                    queues.Add(new Queue { l = queue.l - 1, r = queue.r, s = queue.s + "(" });                
                if (queue.r > 0)               
                    queues.Add(new Queue { l = queue.l, r = queue.r - 1, s = queue.s + ")" });
                
            }
        }
        return ans;
    }   

}

// @lc code=end

