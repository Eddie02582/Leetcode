class Solution {
public:
    int numDecodings_dfs(string s) {
        // 使用一個記憶化表來儲存已經計算過的結果
        vector<int> memo(s.size(), -1);
        return dfs(s, 0, memo);
    }    
    
    int dfs(string s, int index, vector<int>& memo) {
        // 當 index 到達末尾，意味著成功解碼
        if (index == s.size()) return 1;  
        // 不能以 '0' 開頭
        if (s[index] == '0' ) return 0;     

        // 如果已經計算過這個位置，直接返回結果
        if (memo[index] != -1) {
            return memo[index];
        }

        int step1 = 0, step2 = 0;  
        step1 = dfs(s, index + 1, memo);       

        // 嘗試兩步解碼 (兩個字符)
        if (index + 1 < s.size() && s[index] == '1' || (
			s[index] =='2' && s[index + 1]< '7') ){
                  
                step2 = dfs(s, index + 2, memo);
        }
        // 記錄計算結果
        memo[index] = step1 + step2;       
        return memo[index];
    }
};