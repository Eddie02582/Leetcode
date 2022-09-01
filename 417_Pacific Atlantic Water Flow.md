# Minimum Genetic Mutation


## 原題目:
```
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

```

<image src = "https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg">

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
```


## 思路
BFS/DFS的題目,但是如果單純判斷出發點是否可同時到Pacific(x == 0 or y == 0)或是Atlantic (x == m - 1 or y == n - 1)會TLE,所以要分別從Atlantic和Pacific出發個別記錄能到達的座標,如果有重複表示都可到達


## BFS


#### c++


``` C++
class Solution {
public:   
    int m ,n;
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
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
 
};
```

## DFS

#### c++
```
class Solution {
public:   
    int m ,n;    
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



























```





















```  


