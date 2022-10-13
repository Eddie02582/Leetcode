class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size(),n = grid[0].size();
        vector<vector<bool>> visited (m,vector<bool>(n));
        int maxArea = 0;
        for(int i = 0;i < m;i++){
            for(int j = 0;j<n;j++){
                if(!visited[i][j] && grid[i][j]){
                    visited[i][j] = true;
                    maxArea = max(maxArea,bfs(grid,visited,i,j));
                             
                }               
            }            
        }
        return maxArea;
    }
    int bfs(vector<vector<int>>& grid,vector<vector<bool>> & visited,int x,int y){
        int area = 0;
        int m = grid.size(),n = grid[0].size();
        queue<vector<int>> q;
        q.push({x,y});
        vector<vector<int>> adds = {{-1,0},{1,0},{0,1},{0,-1}};
        
        while(!q.empty()){  
            vector<int> cord = q.front();               
            q.pop();
            area+= 1;
            for(auto &add : adds){
                int new_x = cord[0] + add[0];
                int new_y = cord[1] + add[1];
                if(new_x >=0 && new_x < m && new_y >=0 && new_y < n  && grid[new_x][new_y] == 1 && !visited[new_x][new_y]){
                    q.push({new_x ,new_y});
                    visited[new_x][new_y] = true;
                }
            }             
        }
        return area;        
    } 
    int maxAreaOfIsland_dfs(vector<vector<int>>& grid) {
        int m = grid.size(),n = grid[0].size();        
        int maxArea = 0;
        for(int i = 0;i < m;i++){
            for(int j = 0;j< n;j++){
                if(grid[i][j]){                   
                    maxArea = max(maxArea,dfs(grid,i,j));
                             
                }               
            }            
        }
        return maxArea;
    }
    int dfs(vector<vector<int>>& grid,int x,int y){
        int m = grid.size(),n = grid[0].size();
        if(x < 0 || y <0 || x>=m || y >= n || !grid[x][y])
            return 0;
        
        grid[x][y] = 0;
        return 1 +dfs(grid,x + 1,y) + dfs(grid,x - 1,y) +dfs(grid,x,y + 1) +dfs(grid,x,y - 1);       
    }     
};


