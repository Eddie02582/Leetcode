'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                 Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''


#!/usr/bin/python
# encoding=utf-8
class Solution(object):
    def minimumTotal_dfs(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """        

        def dfs (x,y,triangle):
            n = len(triangle)
            if x == n:               
                return 0
            return min(dfs(x + 1, y, triangle), dfs(x + 1, y + 1, triangle)) + triangle[x][y]
     
        if not triangle:
            return -1
        
        result = dfs (0,0,triangle)
        return result    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None                
        p = 1       
        while p <  len(triangle):
            for i in range(p + 1):
                if i == 0 :
                    triangle[p][i] += triangle[p-1][0]
                elif i == p:
                    triangle[p][i] += triangle[p-1][-1]
                else:
                    triangle[p][i] += min(triangle[p - 1][i - 1],triangle[p - 1][i])
            p += 1
        
        return min(triangle[-1])   