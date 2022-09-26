class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {        
        for(int i = 0;i < 9;i++){
            for(int j = 0;j < 9;j++){                
                if (board[i][j] != '.' && !check_duplicate(i,j,board)){
                    return false;
                }         
            }
        }  
        return true;        
    }
    
    
    
    bool check_duplicate(int i,int j,vector<vector<char>>& board){       
       
        for(int col = 0;col< 9;col++){               
            if(col != j & board[i][col] == board[i][j]){                
                   return false;
            }
        }
        for(int row = 0;row< 9;row++){            
            if(row != i & board[row][j]  == board[i][j]){                
                   return false;
            }
        }      
        int start_row = (i/3)*3;
        int start_col = (j/3)*3;
        for(int row = start_row;row < start_row + 3;row++){
            for(int col = start_col;col< start_col + 3;col++){
                if(!(row == i || col== j) & board[row][col] == board[i][j]){                
                   return false;
                }           
            }
        }        
        return true;         
    }
    
    
};

