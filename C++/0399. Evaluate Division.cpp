#include <unordered_map>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    unordered_map<string, vector<pair<string, double>>> graph;

    // 深度优先搜索（DFS）辅助函数
    double dfs(const string& start, const string& end, unordered_map<string, bool>& visited) {
        // 如果起始节点就是终止节点，返回1.0，因为a/a = 1
		if (graph.find(start) == graph.end() || graph.find(end) == graph.end()) 
			return -1.0;
		
        if (start == end) return 1.0;
        
        // 标记当前节点为已访问
        visited[start] = true;

        // 遍历所有相邻的节点
        for (const auto& neighbor : graph[start]) {
            // 如果相邻节点没有被访问过，继续递归搜索
            if (!visited[neighbor.first]) {
                double result = dfs(neighbor.first, end, visited);
                // 如果有有效路径，返回当前边的权值乘以结果
                if (result != -1.0) {
                    return result * neighbor.second;
                }
            }
        }

        // 如果没有找到路径，返回-1
        return -1.0;
    }

    // 主函数，计算多个查询的结果
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        // 第1步：构建图
        for (int i = 0; i < equations.size(); ++i) {
            string start = equations[i][0];
            string end = equations[i][1];
            double value = values[i];
            // 在图中添加双向关系：start -> end = value 和 end -> start = 1/value
            graph[start].emplace_back(end, value);
            graph[end].emplace_back(start, 1.0 / value);
        }

        // 第2步：处理查询
        vector<double> result;
        for (const auto& query : queries) {
            string start = query[0], end = query[1];
            unordered_map<string, bool> visited; // 用于DFS标记已访问的节点
            result.push_back(dfs(start, end, visited)); // 对每个查询进行DFS搜索
        }

        return result;
    }
};