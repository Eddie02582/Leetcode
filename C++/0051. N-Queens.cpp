class Solution {
public:
	vector<vector<string>> ret;

    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
		dfs(0,board);
		return ret;
		
    }
	
	void dfs(int row,vector<string> &board){
		//表示放滿
        int n = board.size();
		if(row == n){
			ret.push_back(board);
			return;
		}
		//loop col
		for(int j = 0;j<n;j++){
			if(isVaild(row,j,board)){
				board[row][j] = 'Q';	
				dfs(row +1,board);
				board[row][j] = '.';
			}
		}		
	}
	bool isVaild(int row,int col,vector<string> &board){
		//check col
		int n = board.size();
		for(int i = 0;i<n;++i){
			if(board[i][col] == 'Q')
				return false;
		}	
		//確認左上
		int count = 0;
		while(row - count >=0 && col - count>=0){
			if(board[row - count][col - count] == 'Q'){
				return false;
			}
			count++;
		}
        //確認右上
        count = 0;
        while (row - count >= 0 && col + count < n) {  // 使用 col + count 来递减
            if (board[row - count][col + count] == 'Q') {
                return false;
            }
            count++;
        }

		return true;
		
	}
	
};









