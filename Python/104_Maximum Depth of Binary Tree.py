# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        print (root.val)
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


root = TreeNode(3)
root.left = TreeNode(9)  
root.right = TreeNode(20)  
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
sol.maxDepth(root)