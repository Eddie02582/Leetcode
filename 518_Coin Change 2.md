# Coin Change 2


## 原題目:
```
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:
    Input: amount = 5, coins = [1, 2, 5]
    Output: 4
    Explanation: there are four ways to make up the amount:
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1
    
Example 2:

    Input: amount = 3, coins = [2]
    Output: 0
    Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

    Input: amount = 10, coins = [10] 
    Output: 1
```

## 思路dp



#### Python
``` python
class Solution(object):
    def change__(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        elif not coins:
            return 0
        
        
        dp = [ [0] * (amount + 1) for _ in range(len(coins))]
        for i in range(len(coins)):    
            for j in range(amount + 1):            
                if j == 0:
                    dp[i][j] = 1
                elif j>= coins[i]:
                    dp[i][j] = dp[i][j - coins[i]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]        
        return dp[-1][amount]
``` 


每次只與前一個狀態更新,dp[i][j] = dp[i][j - coins[i]] + dp[i - 1][j],當走到j時,dp[i][j - coins[i]]已經被更新,可以化簡成dp[j] = dp[j - coins[i]] + dp[j],



``` python
class Solution(object):
    def change(self, amount, coins):     
        if amount == 0:
            return 1
        elif not coins:
            return 0
       
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):    
            for j in range(coins[i],amount + 1):                    
                dp[j] = dp[j - coins[i]] + dp[j]
        return dp[-1] 
``` 














