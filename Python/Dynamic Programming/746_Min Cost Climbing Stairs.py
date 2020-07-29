'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
    
Example 2:
    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6
    Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
    cost will have a length in the range [2, 1000].
    Every cost[i] will be an integer in the range [0, 999].

'''


#!/usr/bin/python
# encoding=utf-8
#070_Climbing Stairs 變型

class Solution(object):
    def minCostClimbingStairs(self, cost):
        table = [0] * (len(cost) +  1)
        table[1] = cost[0]
        for i in range(2,len(cost) + 1):
            table[i] = min(table[i - 1] ,table[i - 2]) + cost[i - 1]  
        return min(table[-1],table[-2])



sol =Solution()

assert sol.minCostClimbingStairs([10, 15, 20])==15

assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])

'''

minCostClimbingStairs_array
[1, 100, 2, 3, 3, 103, 4, 5, 104, 6, 6]

minCostClimbingStairs_last
[1, 100, 2, 3, 3, 103, 4, 5, 104, 6, 6]

minCostClimbingStairs
[1, 100, 2, 3, 3, 103, 4, 5, 104, 6]

'''








