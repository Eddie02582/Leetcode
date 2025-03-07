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


## 思路dp

動態規劃的狀態定義：
我們可以使用一個 dp 陣列來表示不同的狀態。
	狀態 1 (持有股票)：記錄目前持有股票時的最大利潤。
	狀態 2 (不持有股票)：記錄目前不持有股票時的最大利潤。

動態


## Code



``` c++
class Solution {
public:
	int maxProfit(vector<int>& prices) {
		int n = prices.size();
		if (n == 0) return 0;

		// dp[i][0] 表示第 i 天不持有股票的最大利潤
		// dp[i][1] 表示第 i 天持有股票的最大利潤
		vector<vector<int>> dp(n, vector<int>(2));

		// 初始状态
		dp[0][0] = 0; // 第一天不持有股票的利潤為0
		dp[0][1] = -prices[0]; // 第一天買進股票的利潤為 -prices[0]

		for (int i = 1; i < n; i++) {
			// 不持有股票：可以是昨天不持有股票，或今天賣出股票
			dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]);
			// 持有股票：可以是昨天持有股票，或今天買入股票
			dp[i][1] = max(dp[i-1][1], -prices[i]);
		}

		// 最後一天不持有股票時的最大利潤
		return dp[n-1][0];
	}

};


``` 
簡化
``` c++
class Solution {
public:
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    if (n == 0) return 0;

    // 初始化变量
    int prev_not_hold = 0;   // 第一天不持有股票的最大利润
    int prev_hold = -prices[0]; // 第一天持有股票的最大利润

    for (int i = 1; i < n; i++) {
        // 更新持有股票和不持有股票的最大利润
        int new_prev_not_hold = max(prev_not_hold, prev_hold + prices[i]);
        int new_prev_hold = max(prev_hold, -prices[i]);

        // 更新状态
        prev_not_hold = new_prev_not_hold;
        prev_hold = new_prev_hold;
    }

    // 最后一天不持有股票时的最大利润
    return prev_not_hold;
}

};


```





## 思路 貪心演算法解法

1. **初始化變數**：
 - `minPirce = INT_MAX`：用來記錄遇到的最低股價。
 - `ans = 0`：用來記錄目前的最大利潤。

2. **遍歷股票價格**：
 - 以每一個價格，更新最低價格 `minPirce` 為當前價格和先前最低股價中的較小值。
 - 計算當前利潤 `price - minPirce`，並與已有的最大利潤 `ans` 進行比較，更新 `ans` 為較大者。

3. **返回最終最大利潤**。
 
``` c++       
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPirce = INT_MAX;
        int ans = 0;
        for(int price : prices){
            minPirce = min(minPirce,price);         
            ans = max(price - minPirce,ans);
        }        
        return ans;
    }
};

```  
















