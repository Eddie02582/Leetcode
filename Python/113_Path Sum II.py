# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:         
    def pathSum(self, root: TreeNode, targetSum):
        ans = []  
        def backtracking(node,path,path_res):
            if not node:
                return             
            path +=[node.val]  
            path_res -= node.val         
            if not node.left and not node.right and path_res == 0:
                ans.append(path[:])
            else:
                backtracking(node.left,path,path_res)
                backtracking(node.right,path,path_res)                 
            path.pop(-1)



        backtracking(root,[],targetSum)
        return ans        
            

