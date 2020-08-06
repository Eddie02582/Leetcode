# Network Delay Time


## 原題目:
```
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:
 
    1    1     1
1 <-- 2 --->3 ---->4 


Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

    N will be in the range [1, 100].
    K will be in the range [1, N].
    The length of times will be in the range [1, 6000].
```

## 思路
Dijkstra’s 演算法
```

```

#### Python
``` python
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
``` 


``` python
class Solution(object):
    def networkDelayTime_(self, times, N, K):
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N+1)}
        seen = [False] * (N + 1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N + 1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1  
``` 










