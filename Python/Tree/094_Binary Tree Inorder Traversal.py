# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """   
        if root is None:            
            return []
        else:
            #print (root.val)
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

     
    def inorderTraversal_helper(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def hepler(root,result):
            if root:
                hepler(root.left,result)
                result.append(root.val)
                hepler(root.right,result)        
            return result
        
        return hepler(root,[])
        
    def inorderTraversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        visited = set()
        if(not root):
            return res
        queue = [root]
        while(queue):
            curr = queue.pop()
            if(curr not in visited):
                visited.add(curr)
                if(curr.right):
                    queue.append(curr.right)
                queue.append(curr)
                if(curr.left):
                    queue.append(curr.left)
            else:
                res+=[curr.val]
        return res          
        
        
    def inorderTraversal_iterate(self, root):
        result = []
        s = []
        while root is not None or s:                     
            if root is not None:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                result.append(root.val)
                root = root.right
        return result       
        
        
root = TreeNode(1)
root.left = TreeNode(2)  
root.right = TreeNode(3)  
root.left.left = TreeNode(4)  
root.left.right = TreeNode(5)  
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

#root = TreeNode(1) 
#root.right = TreeNode(2) 
#root.right.left = TreeNode(3)



sol = Solution()

print (sol.inorderTraversal(root))
sol.inorderTraversal_iterate(root)










        
        
        
        
        
        
        
        
        
        
        