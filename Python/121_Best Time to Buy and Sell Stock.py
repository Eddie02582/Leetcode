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
    
    def maxProfit_force(self, prices):
        if len(prices) <2:
            return 0
        
        Profit =0   
        count=0

        for i in range (len(prices)-1):
            Profit = max( max(prices[i:])-prices[i] ,Profit)
        return Profit
    #timeout
    def maxProfit_force_simple(self, prices):
        if len(prices) <2:
            return 0        
        Profit,count = 0,0         

        for i in range (len(prices)-1):
            for j in range(j,len(prices)):
                sell = prices[j]
                if prices[j] - prices[i] > Profit:
                    Profit = prices[j] - prices[i]
        return Profit

    
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0        
        minprice = 2**31
        Profit=0
        for i in range (0,len(prices)):
            if prices[i] < minprice:
                    minprice = prices[i]
            elif (prices[i] - minprice) > Profit:
                Profit=prices[i] - minprice            
        
        return Profit

    def maxProfit2(self, prices):
        if len(prices) < 2:
            return 0
        max_profit, min_prev = 0, prices[0]
        for p in prices[1:]:
            if p < min_prev:
                min_prev = p
            else:
                max_profit = max(max_profit, p - min_prev)
        return max_profit
     



    
sol =Solution()


assert sol.maxProfit([7,1,5,3,6,4])==5

assert sol.maxProfit([7,6,4,3,1])==0

assert sol.maxProfit([2,1])==0

assert sol.maxProfit([2,1,2,0,1])==1

assert sol.maxProfit([7,3,7,2,2,4])==4

assert sol.maxProfit2([7,3,7,2,2,4])==4