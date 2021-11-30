class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> dp(m + 1,vector<int>(n + 1));
        int max_square_length = 0;
        for (int i = 0; i < m;i++){
            for (int j = 0;j < n;j++){ 
                if(matrix[i][j] == '1'){
                    if(i == 0 || j == 0)                    
                        dp[i][j] = 1;
                    else
                        dp[i][j] = min({dp[i][j - 1],dp[i - 1][j - 1],dp[i - 1][j]})  + 1;                    
                    max_square_length = max(max_square_length,dp[i][j]);
                }            
            }
        }
        return max_square_length * max_square_length;
    }
};