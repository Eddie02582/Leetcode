class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
            
    def preorderTraversal_helper(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root,res = []):        
            if root:
                res.append(root.val)
                helper(root.left,res)
                helper(root.right,res)
                
            return res
        return helper(root)
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        result = []
        s = []
        s.append(root)
        while s:
            root = s.pop()
            result.append(root.val)
            if root.right:
                s.append(root.right)
            if root.left:
                s.append(root.left)   
        return result