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
``` 












