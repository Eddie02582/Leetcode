/*
 * @lc app=leetcode id=129 lang=csharp
 *
 * [129] Sum Root to Leaf Numbers
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
public class Solution {
    public int SumNumbers(TreeNode root) {

        return getSum(root,0);
    }

    public int getSum(TreeNode root, int sum){
        if (root == null)                
            return 0;
        sum += root.val;

        if (root.left == null && root.right == null) 
            return sum;

        return getSum(root.left, sum * 10) + getSum(root.right, sum * 10);
      
    }
}
// @lc code=end

