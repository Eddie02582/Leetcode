class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;
        triangle.push_back({1});
        
        for(int i = 2;i <=numRows;i++){
            vector<int> row;
            for(int j = 0;j<i;j++){
                if(j == 0 || j == i - 1){
                    row.push_back(1);
                }
                else{
                    row.push_back(triangle[i - 2][j - 1] + triangle[i - 2][j]);
                }
            }
            triangle.push_back(row);
        }        
        
        return triangle;
    }
};