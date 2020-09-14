# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def decision(root):
            if not root:
                return [0,0]
            
            leftRob,leftNot = decision(root.left)
            rightRob,rightNot = decision(root.right)     
            
            rootRob = root.val + leftNot + rightNot
            rootNot = max([leftRob + rightRob,leftRob + rightNot,leftNot + rightRob,leftNot + rightNot])
            
            return [rootRob,rootNot]
        
        return max(decision(root))
 

        
        
        
        