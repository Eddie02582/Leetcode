'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''


#!/usr/bin/python
# encoding=utf-8
class Solution(object):
    def maxProfit(self, prices):   
        profit = 0
        for i in range (1,len(prices)):
            if prices[i] > prices[i - 1]:
                profit +=  prices[i] - prices[i - 1]
        return profit
        
class Solution:
    def maxProfit(self, prices):   
        if len(prices) < 2:
            return 0
        valley = prices[0]
        peak = prices[0]
        maxprofit,i = 0,0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            
            maxprofit += peak - valley

        return maxprofit


    
sol =Solution()


assert sol.maxProfit([7,1,5,3,6,4])==5

assert sol.maxProfit([7,6,4,3,1])==0

assert sol.maxProfit([2,1])==0

assert sol.maxProfit([2,1,2,0,1])==1

assert sol.maxProfit([7,3,7,2,2,4])==4

assert sol.maxProfit2([7,3,7,2,2,4])==4