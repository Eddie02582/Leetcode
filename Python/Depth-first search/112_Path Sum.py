# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:                          
    def hasPathSum(self, root: sum):        
        def dfs(node,total):
            total = total + node.val                           
            if node.left and dfs(node.left,total):               
                return True
            if node.right and dfs(node.right,total ):                
                return True
            if not node.left and not node.right and sum == total:
                return True

            return False
        
        if not root:
            return False

        return dfs(root,0)                 
            
sol = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11,TreeNode(7),TreeNode(2))
root.right = TreeNode(8,TreeNode(13),TreeNode(4,None,1))

print (sol.hasPathSum(root,26))

root = TreeNode(1,2,0)

print (sol.hasPathSum(root,1))

