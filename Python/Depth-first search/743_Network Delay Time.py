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
        processed = []

        costs = {}
        for i in range(1,N + 1):
            if i != K:
                costs[i] = float("inf")

        for parent,node,cost in times:
            graph[parent][node] = cost
            if parent == K:
                costs[node] = min(costs[node],cost)

     
        def find_lowest_cost_node():
            lowest_cost = float("inf")
            lowest_cost_node = None
            for node in costs:
                cost = costs[node]
                if cost < lowest_cost and node not in processed:
                    lowest_cost = cost
                    lowest_cost_node = node
            return lowest_cost_node       

    
        node = find_lowest_cost_node()
        while node is not None:
            cost = costs[node]
            neighbors = graph[node]
            for n in neighbors.keys():
                if n != K:
                    new_cost = cost + neighbors[n]
                    if costs[n] > new_cost:
                        costs[n] = new_cost                    
            processed.append(node)
            node = find_lowest_cost_node()    

        ans = max(costs.values())

        return -1  if ans ==  float('inf') or ans == -1 else ans
        
        
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
