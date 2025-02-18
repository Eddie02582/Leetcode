class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false); // Pass by reference
        int province = 0;

        // Loop through each node to start DFS if not already visited
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                dfs(isConnected, visited, i); // Start a DFS from the unvisited node
                province++;  // Increase province count after completing DFS
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
	
	int findCircleNum_bfs(vector<vector<int>>& isConnected) {
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


