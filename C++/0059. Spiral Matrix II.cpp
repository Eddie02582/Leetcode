#include <vector> 
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> matrix(n,vector<int>(n,0));
        vector<vector<int>> directions{vector<int>{0,1},vector<int>{1,0},vector<int>{0,-1},vector<int>{-1,0}};
        int direction_mode = 0;
        int x = 0,y = 0;
        int dx = directions[direction_mode][0];
        int dy = directions[direction_mode][1];
        
        for (int i = 1;i <= n*n;i++){
            matrix[x][y] = i;              
            if ( x + dx >= n || x + dx < 0 || y + dy >= n || y + dy < 0 || matrix[x + dx][y + dy] != 0)
            {
                direction_mode = (direction_mode + 1)%4;
                dx = directions[direction_mode][0];
                dy = directions[direction_mode][1];
            }
            x += dx ;
            y += dy;
        }
        return matrix;
    }
};

