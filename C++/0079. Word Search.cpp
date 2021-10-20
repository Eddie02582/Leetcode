#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        vector<vector<bool>> visited (m,vector<bool>(n,false));
        
        for (int i = 0;i<m;i++){
            for (int j = 0;j < n ;j++){
                if(board[i][j] == word[0])
                {
                    visited[i][j] = true;
                    if (backtracking(board,word,visited,i,j,1))
                        return true;
                    visited[i][j] = false;
                }
                
            }  
        }
        return false;       
        
    }
    bool backtracking(vector<vector<char>>& board,string word,vector<vector<bool>> visited,int i,int j,int n){        
        if( n == word.size()){
            return true;
        }
        
        int array[4][2]= {{0,1},{1,0},{0,-1},{-1,0}};    
        
        for(int row = 0;row < 4;row++){  
            int dx = array[row][0];
            int dy = array[row][1];
            if(board[i + dx][j + dy] == word[n] && !visited[i + dx][j + dy])
            {
                visited[i][j] = true;
                if(backtracking(board,word,visited,i +dx ,j + dy,n + 1)){
                    return true;
                }  
                visited[i][j] = false;
            }            
        }
        return false;
        
    }
    
    
};


int main(){
    vector<vector<char>>& board;
    board.push_back(vector<char>{"A","B","C","E"});
    board.push_back(vector<char>{"S","F","C","S"});
    board.push_back(vector<char>{"A","D","E","E"});
    Solution sol;
    string word = "SEE";
    sol.exist(vector<vector<char>>& board, string word);

    
}

















