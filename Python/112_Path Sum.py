# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: sum):        
       if not root: return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val)                 
            
    def hasPathSum(self, root, targetSum):

        def dfs(root,res):            
            if not root:                
                if res == 0:                  
                    return True
                return False
            
            res -= root.val            
            if dfs(root.left,res):
                return True
            if dfs(root.right,res):
                return True
        
        return dfs(root,targetSum)       
            
            
sol = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11,TreeNode(7),TreeNode(2))
root.right = TreeNode(8,TreeNode(13),TreeNode(4,None,1))

print (sol.hasPathSum(root,26))

root = TreeNode(1,2,0)

print (sol.hasPathSum(root,1))

