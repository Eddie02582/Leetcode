# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            q = [root]
            s = [] 
            while q:
                size = len(q)
                level = []
                for i in range(size):
                    node = q.pop(0)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level.append(node.val)
                s.append(level)
        res = [ s.pop() for i in range(len(s))]
            
        return res
            