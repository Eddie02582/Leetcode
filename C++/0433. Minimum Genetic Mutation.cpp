class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        unordered_set<string> bank_set(bank.begin(),bank.end());
        queue<string> que;
        unordered_set<string> visited {start};   
        que.push(start);  
        int step = 0;
        while (!que.empty()){            
            int size = que.size();
            for(int i = 0; i < size;i++){
                string cur = que.front();
                que.pop();
                if(cur == end)
                    return step;
                
                for(char gene :"ACGT"){
                    for (int j = 0;j < cur.size();j++){
                        string next = cur;
                        next[j] = gene;                    
                        if(bank_set.find(next) != bank_set.end() && visited.find(next) == bank_set.end()){
                            que.push(next);                            
                            visited.insert(next);
                        }                        
                    }
                }                
            } 
            step++;
        }     
        return -1;
    }
};