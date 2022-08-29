#  Number of Islands


## 原題目:
```
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:
	Input: grid = [
	  ["1","1","1","1","0"],
	  ["1","1","0","1","0"],
	  ["1","1","0","0","0"],
	  ["0","0","0","0","0"]
	]
	Output: 1
	
Example 2:
	Input: grid = [
	  ["1","1","0","0","0"],
	  ["1","1","0","0","0"],
	  ["0","0","1","0","0"],
	  ["0","0","0","1","1"]
	]
	Output: 3
	 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
```

## 思路DFS

#### c++

```c++
class Solution {
public:
    //dfs
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<bool>> visited (m, vector<bool>(n));       
        int islands = 0;    
        for( int i = 0; i < m;i++){
            for(int j = 0; j < n;j++){                
                if(!visited[i][j] && grid[i][j] == '1'){                 
                    dfs(grid,visited,i,j);          
                    islands += 1;
                }                    
                 
            }

        }             
        
         return islands;
    }
    
    void dfs(vector<vector<char>>& grid,vector<vector<bool>> &visited,int x,int y){    
        int m = grid.size(), n = grid[0].size();
        if (x < 0 || x == m || y <0 || y == n || visited[x][y] || grid[x][y] == '0')
            return;  
        visited[x][y] = true;        
        dfs(grid,visited,x,y - 1); 
        dfs(grid,visited,x,y + 1);
        dfs(grid,visited,x + 1,y);
        dfs(grid,visited,x - 1,y);   
    }     
    
};
```

簡化直接修改grid代表已經拜訪過<br>

<a href = "https://leetcode.com/submissions/detail/786046453/">98%</a>

```
class Solution {
public:
    //dfs
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();        
        int islands = 0;    
        for( int i = 0; i < m;i++){
            for(int j = 0; j < n;j++){                
                if(grid[i][j] == '1'){                 
                    dfs(grid,i,j);          
                    islands += 1;
                }  
            }
        }   
         return islands;
    }    
    void dfs(vector<vector<char>>& grid,int x,int y){    
        int m = grid.size(), n = grid[0].size();
        if (x < 0 || x == m || y <0 || y == n ||  grid[x][y] != '1')
            return;  
        grid[x][y] = '*';        
        dfs(grid,x,y - 1); 
        dfs(grid,x,y + 1);
        dfs(grid,x + 1,y);
        dfs(grid,x - 1,y);   
    }  
};
```






#### Python

``` python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x,y):  
            grid[x][y] = "*"           
            for r,c in [(x + 1,y),(x - 1,y),(x,y - 1),(x, y+ 1)]:
                if 0 <= r < m and 0<= c <n and grid[r][c] == "1":                    
                    dfs(r,c)

        m,n = len(grid),len(grid[0])
        num_island = 0 
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1":                   
                    dfs(x,y)                    
                    num_island += 1        
        return num_island 
``` 






## 思路BFS

#### c++

```c++
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();      
        vector<vector<int>> adds {{0,1},{0,-1},{1,0},{-1,0}};
        int islands = 0;  
        
        for( int i = 0; i < m;i++){
            for(int j = 0; j < n;j++){                
                if(grid[i][j] == '1'){
                    queue <vector<int>> q;          
                    q.push(vector<int>{i,j});
                    grid[i][j] = '*';                    
                    while(!q.empty()){                                        
                        int cur_x = q.front()[0],cur_y = q.front()[1]; 
                        q.pop(); 
                        for( auto add:adds ){
                            int x = cur_x + add[0]; 
                            int y = cur_y + add[1];
                            if(x < m && x >= 0 && y <n && y >=0 && grid[x][y] == '1'){
                                    grid[x][y] = '*';
                                    q.push(vector <int>{x,y});
                                }
                        }
                     }
                    islands += 1;
                }   
            }

        }             
        
         return islands;
    }
};
```





####python

``` python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        m,n = len(grid),len(grid[0])
        num_island = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":                   
                    queue = deque([(i,j)])
                    grid[i][j] == "*"
                    while queue:
                        x,y = queue.popleft()                        
                        for r,c in [(x + 1,y),(x - 1,y),(x,y - 1),(x, y+ 1)]:
                            if 0 <= r < m and 0<= c <n and grid[r][c] == "1":  
                                queue.append((r,c))
                                grid[r][c] = "*"                                      
                    num_island += 1        
        return num_island
```

















