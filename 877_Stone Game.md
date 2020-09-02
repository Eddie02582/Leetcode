# Stone Game


## 原題目:
```
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
```

## 思路動態規劃
以[3,9,1,2],dp[i][j]儲存先手後手的值(fisrt,second)
```
start\end    0     1     2     3
    0      (3,0)  (9,3) (4,9) (11,4)
    1        x    (9,0) (9,1) (10,2)
    2        x      x   (1,0) (2,1)
    3        x      x   (1,0) (2,1)
    
 ```   
[3,9,1,2] ,只能取左邊後右邊 ,取左邊 3 +後手的[9,1,2] ,和 2後手的[3,9,1] 這2個可能的最大値<br>
左邊:(piles[i] + dp[i + 1][j][1],dp[i + 1][j][0])
右邊:(piles[j] + dp[i][j - 1][1],dp[i][j - 1][0])
dp[i][j] = max( 左邊,右邊)

    
    
#### Python
``` python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [ [[0,0]] * n  for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = [piles[i],0]
        
        for i in range(n - 2, - 1,-1):
            for j in range(i + 1,n):
                left = [dp[i + 1][j][1] + piles[i],dp[i + 1][j][0]]
                right = [dp[i][j - 1][1] + piles[j],dp[i][j - 1][0]]

                dp[i][j] = max ( left ,right)         
        return dp[0][n - 1][0] > dp[0][n - 1][1]        
``` 












