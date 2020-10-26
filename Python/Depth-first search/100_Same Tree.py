# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree__(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """      
        
        if not p or not q:
            return p == q       
        
        return q.val == p.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
            
   
    def isSameTree(self, p, q):
        from collections import deque
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True



            
t1 =   TreeNode(1)
t1.left = TreeNode(2)  
  

t2=   TreeNode(1) 
t2.right = TreeNode(2)  


sol = Solution()
sol.isSameTree(t1,t2)        
 