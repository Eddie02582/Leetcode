/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {     
        if (!node)
            return node;
        unordered_map<Node*,Node*> nodes;
        //bfs
        queue<Node*> q;
        q.push(node);   
        nodes[node] = new Node(node->val);
        
        while(!q.empty()){
            int size = q.size();            
            Node* curr = q.front();
            q.pop();  
            for(auto adj:curr->neighbors){     
                if(!nodes[adj]){
                    q.push(adj);                        
                    nodes[adj] =  new Node(adj->val);
                }
                nodes[curr]->neighbors.push_back(nodes[adj]);
            } 
        }
        return nodes[node];
        
    }
};









