# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:         
    def pathSum(self, root, sum):        
        def dfs(node,total,sol):
            total = total + node.val   
            sol = sol + [node.val]                        
            if node.left:
                dfs(node.left,total,sol) 
            if node.right:
                dfs(node.right,total,sol)      
            if not node.left and not node.right :
                if sum == total:
                    res.append(sol[:])
                return          
        res = []
        if not root:
            return []
        dfs(root,0,[])     
        return res            
            

