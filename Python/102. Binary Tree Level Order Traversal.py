# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        queue = []
        queue.append(root)
        output = []
        
        while len(queue) > 0:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop(0)
                
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
                    
                level.append(node.val)
                
            output.append(level)
            
        return output

    def levelOrder_level(self, root) :
        self.res = []
        self.level_scan(root, 1)
        return self.res
    
    def level_scan(self, node, level):
        
        if node:
            if len(self.res) < level:
                self.res.append([])
            self.res[level-1].append(node.val)
        else:
            return
        if node.left:
            self.level_scan(node.left, level+1)
        if node.right:
            self.level_scan(node.right, level+1)


root = TreeNode(3)
root.left = TreeNode(9)  
root.right = TreeNode(20)  
# root.left.left = TreeNode(4)  
# root.left.right = TreeNode(5)  
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
sol.levelOrder(root)