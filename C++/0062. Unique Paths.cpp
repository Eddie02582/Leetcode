// Your First C++ Program

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {      
        vector<int> dp;
        for (int i = 0;i < n;i ++){
            dp.push_back(1);
        }
        
        for (int i = 1;i<m;i++){
            for (int j = 1;j <n ;j++){
                dp[j] = dp[j] + dp[j - 1];  
            }            
        }        
        return dp[n - 1];
    }
};

int main() {
	Solution sol;
	sol.uniquePaths(2,1);
}