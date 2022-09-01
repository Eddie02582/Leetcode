class Solution {
public:   
    int m ,n;
    
    vector<vector<int>> pacificAtlantic_bfs(vector<vector<int>>& heights) {
        m = heights.size(),n = heights[0].size();   
        vector<vector<int>> ans;  
        vector<vector<bool>> canPacific(m,vector<bool>(n)); 
        vector<vector<bool>> canAtlantic(m,vector<bool>(n));
        
        //Pacific
        //for top
        vector<vector<int>> start1;
        for (int j = 0; j < n;j++){          
            bfs(heights,canPacific,0,j);
        }
        for (int i = 0; i < m;i++){
            bfs(heights,canPacific,i,0);
        }
        
        for (int j = 0; j < n;j++){
            bfs(heights,canAtlantic,m - 1,j);
        }
        for (int i = 0; i < m;i++){
            bfs(heights,canAtlantic,i,n - 1);
        } 
      
        canPacific[0][n - 1] =true;
        canAtlantic[m - 1][0] = true;  
        
        for (int i = 0; i < m;i++){
            for (int j = 0; j < n;j++){
                if(canPacific[i][j] && canAtlantic[i][j]) 
                    ans.push_back(vector<int>{i,j});
            }            
        }   
        return ans;   
            
    }
    
    void bfs(vector<vector<int>>& heights,vector<vector<bool>>& canFlow,int x,int y){  
        if(canFlow[x][y])
            return;
        vector<vector<int>> paths = {{1,0},{-1,0},{0,1},{0,-1}};    
        queue<vector<int>> q;
        q.push(vector<int>{x,y});
        canFlow[x][y] = true;
        while(!q.empty()){
            int cx = q.front()[0],cy = q.front()[1];
            q.pop();
            for(auto path :paths){
                int nx = cx + path[0],ny = cy + path[1];                       
                if( nx >= 0 && nx < m && ny >=0 && ny <n && heights[nx][ny] >= heights[cx][cy] && !canFlow[nx][ny]){
                    q.push(vector<int>{nx,ny});
                    canFlow[nx][ny] = true;                  
                }                
            } 
        }      
    }
    
    
    
    vector<vector<int>> pacificAtlantic_dfs(vector<vector<int>>& heights) {
        m = heights.size(),n = heights[0].size();   
        vector<vector<int>> ans;
        vector<vector<bool>> canPacific(m,vector<bool>(n)); 
        vector<vector<bool>> canAtlantic(m,vector<bool>(n));    
        
        for (int j = 0; j < n;j++){
            dfs(heights,canPacific,0,j);
        }
        for (int i = 0; i < m;i++){
            dfs(heights,canPacific,i,0);
        }
        
        for (int j = 0; j < n;j++){
            dfs(heights,canAtlantic,m - 1,j);
        }
        for (int i = 0; i < m;i++){
            dfs(heights,canAtlantic,i,n - 1);
        }  
        for (int i = 0; i < m;i++){
            for (int j = 0; j < n;j++){
                if(canPacific[i][j] && canAtlantic[i][j]) 
                    ans.push_back(vector<int>{i,j});
            }            
        }    
        return ans;   
            
    }
    
    void dfs(vector<vector<int>>& heights,vector<vector<bool>>& canFlow,int x,int y){
        if (canFlow[x][y])
            return;
        canFlow[x][y] = true;
        if(x + 1 < m && ! canFlow[x + 1][y] && heights[x + 1][y] >= heights[x][y]){
            dfs(heights,canFlow,x + 1,y);
        }
        if(x - 1 >= 0 && ! canFlow[x - 1][y] && heights[x - 1][y] >= heights[x][y]){
            dfs(heights,canFlow,x - 1,y);
        }  
        if(y + 1 <  n&& ! canFlow[x][y + 1] && heights[x][y + 1] >= heights[x][y]){
            dfs(heights,canFlow,x,y + 1);
        }
        if(y - 1 >=0 && ! canFlow[x][y - 1] && heights[x][y - 1] >= heights[x][y]){
            dfs(heights,canFlow,x,y - 1);
        } 
    } 
    
 
};
























