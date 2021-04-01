/*
 * @lc app=leetcode id=113 lang=csharp
 *
 * [113] Path Sum II
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 using System.Collections.Generic;
 public class Solution {
        public IList<IList<int>> PathSum(TreeNode root, int targetSum)
        {
            IList<IList<int>> ans = new List<IList<int>>();            
            getPathSum(root, targetSum, new List<int>(), ans);
            return ans;
        }

        public void getPathSum(TreeNode root, int path_res, IList<int> path, IList<IList<int>> ans)
        {                        
            if (node == null)
                return;

            path.Add(node.val);
            path_res = path_res - node.val;               
            getPathSum(node.left, path_res, new List<int>(path), ans);  
            getPathSum(node.right, path_res, new List<int>(path), ans);  
            if (node.left == null && node.right == null && path_res == 0)           
                ans.Add(path);
            

        }

}
// @lc code=end

