# Best Time to Buy and Sell Stock


## 原題目:
```
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
```
Example 1:
```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
             
```

Example 2:
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```


## 思路
一般想法由指針i由後往前,指針j由i-1 到零,取出prices[i]-prices[j]最小值,這方法會timeout






## Code



``` python
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        for i in range (len(prices) - 1,0,-1):
            for j in range (i - 1,-1,-1):
                max_profit = max (max_profit,prices[i]-prices[j])
        return max_profit
``` 


## 思路
利用min_prev 計錄當天之前最小值,迴圈從1開始賣,當天賣出最大值即為price-min_buy

 
``` python       
class Solution:   
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
    
        buy = float('inf') 
        profit = 0
        for n in prices:
            if n < buy:
                buy = n 
            profit = max(sell - buy,profit)        
        return profit
        
```  
















