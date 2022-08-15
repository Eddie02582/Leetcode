# Minimum Genetic Mutation


## 原題目:
```
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.


Example 1:
    Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
    Output: 1
    
Example 2:
    Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    Output: 2
    
Example 3:
    Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
    Output: 3
 

Constraints:
    start.length == 8
    end.length == 8
    0 <= bank.length <= 10
    bank[i].length == 8
    start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

```

## BFS
從start開始,將每個位置個個別替換一個字母,判斷字母是否在bank裡面,如果在bank裡面加入下次的queue


#### c++


``` C++
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
```  


