class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
		int rowCount = grid.size();
		int colCount = grid[0].size();		
		int pairsCount = 0;
		vector<vector<int>> colDatas;
		
		//儲存colDatas
		for(int col = 0;col<colCount;col++){
			vector<int> colData;
			for(int row = 0;row<rowCount;row++){
				colData.push_back(grid[row][col]);			
			}
			colDatas.push_back(colData);
		}
		//一一檢查 
        for(int col = 0;col<colCount;col++){
			for(int row = 0;row<rowCount;row++){
				if(colDatas[col] == grid[row])
					pairsCount++;
			}			
		}
		return pairsCount;
    }
};