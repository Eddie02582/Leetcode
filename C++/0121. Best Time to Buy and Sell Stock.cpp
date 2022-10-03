class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0];        
        int profit = 0; 
        for(auto n:prices){
            if (n < buy)
                buy = n;            
            if(n - buy > profit)
              profit = n - buy;            
        }
        return profit;
    }
};