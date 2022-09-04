# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = {}
        
        queue = deque([(root,0,0)])
        while (queue):
            size = len(queue)
            for i in range(size):
                node,col,row = queue.popleft()   
                if col not in col_map:
                    col_map[col] = {}
                    col_map[col][row] = []
                col_map[col][row].append(node.val)  
                if node.left:                
                    queue.append((node.left,col- 1,row + 1))
                if node.right:                
                    queue.append((node.right,col + 1,row + 1))
        ans = []    
        for colname in  list(sorted(col_map.keys())):  
            sub_ans = []
            for rowname in list(sorted(col_map[colname].keys())):  
                sub_ans += sorted(col_map[colname][rowname])
            ans.append(sub_ans)        
        return ans
      