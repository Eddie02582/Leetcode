class Solution(object):        
    def integerReplacement(self, n: int) -> int:
        from collections import deque
        queue = deque([n])        
        
        level = 0
        while queue:
            length = len(queue)            
            for i in range(length):
                node = queue.popleft()
                if node == 1:
                    return level           
                elif node % 2:
                    queue += [node + 1,node - 1]
                else:
                    queue.append(node//2)               
            level += 1      
        
        return -1

    def integerReplacement(self, n: int) -> int:
        ans = float('inf')
        def dfs(node,level):
            nonlocal ans
            if node == 1:
                ans = min(ans,level)
                return          
            if node % 2:
                dfs(node + 1 ,level + 1)
                dfs(node - 1, level + 1)
            else:
                dfs(node // 2 ,level + 1)            
         
        dfs(n,0)        
        return  ans  
        
    def integerReplacement(self, n: int) -> int:        
        def dfs(node):           
            if node == 1:                
                return 0         
            if node % 2:
                return min(dfs(node + 1),dfs(node - 1)) + 1
            else:
                return dfs(node // 2) + 1   
        return  dfs(n)     