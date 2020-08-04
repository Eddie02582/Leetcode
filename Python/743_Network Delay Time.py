class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict
        graph = defaultdict(dict)
        visited = defaultdict(dict)
        for parent,node,cost in times:
            graph[parent][node] = cost
            visited[parent][node] = False
     
        costs = [float('inf')] * (N + 1)
        costs[K] = 0
        costs[0] = 0
    
        queue = [K]
        
        while queue:
            n = queue.pop(0)            
            for neighborhood in graph[n].keys():
                costs[neighborhood] = min(costs[neighborhood],costs[n] + graph[n][neighborhood]) 
                if not visited[n][neighborhood]:
                    queue.append(neighborhood)
                    visited[n][neighborhood] = True

            
        return max(costs) if all (cost !=float('inf')  for cost in costs) else -1
        
        
sol = Solution()

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2       
sol.networkDelayTime(times,N,K)


N = 5
K = 3 
times = [[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]]

sol.networkDelayTime(times,N,K)


times = [[1,2,1]]
N = 2
K = 2       
print (sol.networkDelayTime(times,N,K))
