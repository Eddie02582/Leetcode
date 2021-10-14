# Perfect Squares


## 原題目:
```
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

## 思路
dp,先建立可以換的數字,就會變成coin change

以n = 12 為例
建立dp表
<table>
    <tr>
        <td>square/n</td>
        <td>0</td>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
        <td>7</td>
        <td>8</td>
        <td>9</td>
        <td>10</td>      
        <td>11</td>
        <td>12</td>     
    </tr>
    <tr>
        <td>1</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>      
        <td></td>
        <td></td>
        <td></td>        
    </tr>
    <tr>
        <td>4</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>      
        <td></td>
        <td></td>
        <td></td>        
    </tr>
    <tr>
        <td>9</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>      
        <td></td>
        <td></td>
        <td></td>      
    </tr>
</table>

第一次只有square = 1的選擇,dp[i] = dp[i] + dp[i - square],
<table>
    <tr>
        <td>0</td>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
        <td>7</td>
        <td>8</td>
        <td>9</td>
        <td>10</td>      
        <td>11</td>
        <td>12</td>     
    </tr>
</table>

第二次多了只有square = 4的選擇,在i < square 不用管,因為n不夠兌換,= 1,dp[i] = min(dp[square] + dp[i - square],dp[i])



#### Python

``` python
class Solution:
    def numSquares(self, n: int) -> int:
        coins = [ i * i for i in range(1, int(n**0.5) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
    
        for i in range(1, n + 1):
            dp[i] = min([1 + dp[i - coin] for coin in coins])          
        return dp[-1]     
``` 

#### C++


```c++
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int numSquares(int n) {     
        vector<int> dp;
        for (int i = 0;i < n + 1;i++){     
            dp.push_back(INT_MAX );
        } 
        dp[0] = 0;
        
        vector<int> choices;
        for (int i = 1;i *i <= n;i++){
            choices.push_back(i * i);
        }    

        for(int choice : choices){
            for (int j = choice;j < n + 1;j++){
                if (dp[j] > dp[j - choice] + 1)
                    dp[j] = dp[j - choice] + 1;
            }

        }
        return dp[n];     
    }
};
```


```c++
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int numSquares(int n) { 
    
        vector<int> dp;
        for (int i = 0;i < n + 1;i++){     
            dp.push_back(INT_MAX );
        } 
        dp[0] = 0;
        
        vector<int> choices;
        for (int i = 1;i *i <= n;i++){
            choices.push_back(i * i);
        }   
        for (int i = 0;i < n + 1;i ++ ){
            for (int j = 0;j < choices.size();j++){
                if(i >= choices[j]){
                    int choice = choices[j];
                    if (dp[i] >1 + dp[i - choice])
                        dp[i] = 1 + dp[i - choice];
                }

            }
        }
        return dp[n];     
    }
};
```




