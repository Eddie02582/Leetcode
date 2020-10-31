# Predict the Winner

這題與 <a href = "https://github.com/Eddie02582/Leetcode/blob/master/877_Stone%20Game.md">Stone Game</a>題目雷同

## 原題目:
```
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:

Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
 

Example 2:

Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
 

Constraints:

1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
```

## 思路動態規劃
以[1, 5, 233, 7],dp[i][j]儲存先手後手的值(fisrt,second)
```
start\end    0     1     2     3
    0      (3,0)  (9,3) (4,9) (11,4)
    1        x    (9,0) (9,1) (10,2)
    2        x      x   (1,0) (2,1)
    3        x      x   (1,0) (2,1)
    
 ```   
[1,5,233,7] ,只能取左邊後右邊 ,取左邊 1 +後手的[5,233,7] ,和 7後手的[1,5,233] 這2個可能的最大値<br>
左邊:(piles[i] + dp[i + 1][j][1],dp[i + 1][j][0])
右邊:(piles[j] + dp[i][j - 1][1],dp[i][j - 1][0])
dp[i][j] = max( 左邊,右邊)

    
    
#### Python
``` python
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        m = len(nums)
        dp = {}
       
        for i in range(m):
            dp[(i,i)] = [nums[i],0]
            
        
        for i in range(m - 1,-1,-1):
            for j in range(i + 1,m):
                choose1 = [nums[j] + dp[(i,j - 1)][1],dp[(i,j - 1)][0]]  
                choose2 = [nums[i] + dp[(i + 1,j)][1], dp[(i + 1,j)][0]]   
                dp[(i,j)] = max(choose1 ,choose2)
        
        
        return dp[(0,m - 1)][0] >= dp[(0,m - 1)][1]      
``` 












