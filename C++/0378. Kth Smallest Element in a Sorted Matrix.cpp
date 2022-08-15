class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        vector<int> indexs(n); 
        int minRow = 0;
        while(k){            
            minRow = -1;
            for(int i = 0;i < matrix.size();i++){
                if(indexs[i] <matrix[i].size()){
                    if(minRow == -1 || matrix[i][indexs[i]] < matrix[minRow][indexs[minRow]] )                   
                        minRow = i;                   
                }
            }   
            k--;
            if(k == 0)
                return matrix[minRow][indexs[minRow]];
            indexs[minRow]++;
        }
        return 0;
    }
};