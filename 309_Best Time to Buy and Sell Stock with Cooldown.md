# Best Time to Buy and Sell Stock with Cooldown


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
## 動態規劃分析

這道題的關鍵是如何在三種狀態之間進行狀態轉移，特別是冷卻期狀態的處理。


### 主要狀態

我們可以定義三個主要的狀態：

1. **`hold[i]`**: 在第 `i` 天持有股票的最大利潤。
2. **`not_hold[i]`**: 在第 `i` 天不持有股票且不在冷卻期中的最大利潤。
3. **`cooldown[i]`**: 在第 `i` 天處於冷卻期的最大利潤。


### 冷卻期的難點

冷卻期的特殊性在於，它只能在賣出股票後進入，並且一旦進入冷卻期，不能在冷卻期內進行買入或賣出的操作。因此，在推導狀態轉移方程時，必須特別處理冷卻期。

### 狀態轉移方程

1. **`hold[i]`**：表示在第 `i` 天持有股票的最大利潤，來自兩種情況：
   - 繼續持有股票：`hold[i-1]`
   - 從 `not_hold[i-1]` 狀態轉移過來，即買入股票：`not_hold[i-1] - prices[i]`

   公式：
   ```cpp
   hold[i] = max(hold[i-1], not_hold[i-1] - prices[i])
   ```

2. **`not_hold[i]`**：表示在第 i 天不持有股票且不在冷卻期的最大利潤，來自兩種情況：
	- 繼續不持有股票：not_hold[i-1]
	- 從冷卻期轉移過來：cooldown[i-1]
   公式：
   ```cpp
   not_hold[i] = max(not_hold[i-1], cooldown[i-1])

   ```

2. **`cooldown[i]`**：表示在第 i 天處於冷卻期的最大利潤，只能來自以下一種情況：
	- 從前一天的 hold[i-1] 狀態轉移過來，即賣出股票並進入冷卻期：hold[i-1] + prices[i]
	
   公式：
   ```cpp
   cooldown[i] = hold[i-1] + prices[i]


   ```
```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n == 0) return 0;

        // 初始化狀態
        int hold = -prices[0];      // 第0天買入股票
        int not_hold = 0;           // 第0天不持股
        int cooldown = 0;           // 第0天冷卻期

        // 從第1天開始遍歷
        for (int i = 1; i < n; ++i) {
            int new_hold = max(hold, not_hold - prices[i]);        // 繼續持有或買入
            int new_not_hold = max(not_hold, cooldown);            // 繼續不持股或從冷卻期轉為不持股
            int new_cooldown = hold + prices[i];                   // 從持股轉到冷卻期

            hold = new_hold;
            not_hold = new_not_hold;
            cooldown = new_cooldown;
        }

        // 最終結果：最大利潤可能是進入冷卻期的利潤或不持股的利潤
        return max(not_hold, cooldown);
    }
};
```



