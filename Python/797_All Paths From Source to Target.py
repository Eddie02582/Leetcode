class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        goal = len(graph) - 1
        def backtracking(pos,sol,prev):
            if  prev == goal:
                ans.append(sol[::])
                return            
            for n in  graph[pos]:
                backtracking(n,sol + [n],n)        
        
        backtracking(0,[0],0)        
        return ans      
        