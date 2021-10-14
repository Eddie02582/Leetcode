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

    int numSquares_dp(int n) { 
    
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

int main()
{
    Solution sol;
    sol.numSquares_dp(12);

}