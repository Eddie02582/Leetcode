class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int side = n;
        int x = 0, y = 0;
        
        for (int side = n ; side > 1;side -=2 ){
            for(int k = 0;k < side - 1;k++){
                int temp = matrix[x][y + k];   
            
                //left top  = left bottom     
                matrix[x][y + k] = matrix[n - 1 - k][y];
                
                //left bottom  = rigt bottom     
                matrix[n - 1 - k][y] = matrix[n - 1][n - 1 - k];  
               
                //rigt bottom  = rigt top      
                matrix[n - 1][n - 1 - k] = matrix[x + k][n - 1];                    
              
                //rigt top  = left top      
                matrix[x + k][n - 1] = temp; 
            }
            n--;    
            x++;
            y++;            
        } 
    }
};