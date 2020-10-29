class Solution(object):
    def canReach_dfs(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """  
        visited = [False] * len(arr)
        
        def dfs(index):   
            if arr[index] == 0:
                return True

            for j in [index - arr[index] ,index + arr[index]]:
                if 0 <= j < len(arr) and not visited[j]: 
                    visited[j] = True
                    if dfs(j):
                        return True
                    visited[j] = False  
            return False   
            
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """  
        visited = [False] * len(arr)        
        queue = [start]

        while queue:
            length = len(queue)
            for i in range(length):
                index = queue.pop(0)
                if arr[index] == 0:
                    return True
                for j in [index - arr[index] ,index + arr[index]]:
                    if 0 <= j < len(arr) and not visited[j]:              
                        queue.append(j)   
        return False 