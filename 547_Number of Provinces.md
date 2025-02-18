# Number of Provinces

## 原題目:
```
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:
	Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
	Output: 2
	
Example 2:
	Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
	Output: 3
 

Constraints:
	1 <= n <= 200
	n == isConnected.length
	n == isConnected[i].length
	isConnected[i][j] is 1 or 0.
	isConnected[i][i] == 1
	isConnected[i][j] == isConnected[j][i]
```


## DFS

#### c++
``` c++
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
		int n = isConnected.size();
        vector<bool> visited(n,false);
		int province = 0;		
		for (int i = 0;i < n; ++i){
			if(!visited[i]){				
				dfs(isConnected,visited,i);				
				province += 1;
			}
		}
		return province;
    }
    void dfs(vector<vector<int>>& isConnected, vector<bool>& visited, int currNumber) {
        visited[currNumber] = true; // Mark the current node as visited
        // Visit all connected nodes
        for (int i = 0; i < isConnected[currNumber].size(); ++i) {
            if (isConnected[currNumber][i] == 1 && !visited[i]) { // Only visit unvisited connected nodes
                dfs(isConnected, visited, i); // Recur for connected node
            }
        }
    }
	
};



``` 

## BFS

#### c++
```c++
class Solution {
public:	
	int findCircleNum(vector<vector<int>>& isConnected) {
		int n = isConnected.size();
		vector<bool> visited(n, false);
		queue<int> q;
		int province = 0;

		for (int cityNumber = 0; cityNumber < n; ++cityNumber) {
			if (visited[cityNumber]) continue;  // 如果這個城市已經被訪問過，跳過
			q.push(cityNumber);  // 將城市加入隊列
			visited[cityNumber] = true;  // 標記為已訪問

			// 執行 BFS
			while (!q.empty()) {
				int currCityNumber = q.front();
				q.pop();
				for (int j = 0; j < isConnected[currCityNumber].size(); ++j) {
					if (!visited[j] && isConnected[currCityNumber][j] == 1) {
						visited[j] = true;  // 標記鄰居為已訪問
						q.push(j);  // 將鄰居加入隊列
					}
				}
			}
			province++;  // 一次 BFS 完成後，表示找到一個省份
		}

		return province;  // 返回省份的數量
	}
	
	
};




```












