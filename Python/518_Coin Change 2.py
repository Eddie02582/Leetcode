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
        
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
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

sol = Solution()
sol.change__(5,[1, 2, 5])
 
 

sol = Solution()
sol.change(5,[1, 2, 5])
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 