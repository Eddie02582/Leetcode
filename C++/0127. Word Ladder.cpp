#include<unordered_set>
#include<vector>
#include<string>
#include<queue>
using namespace std;
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string>  wordList_set(wordList.begin(),wordList.end());
        queue<string> que;
        unordered_set<string> visited {beginWord};   
        que.push(beginWord);  
        int step = 1;
        while (!que.empty()){            
            int size = que.size();
            for(int i = 0; i < size;i++){
                string cur = que.front();
                que.pop();
                if(cur == endWord)
                    return step;
                
                for(char gene :"abcdefghijklmnopqrstuvwxyz"){
                    for (int j = 0;j < cur.size();j++){
                        string next = cur;
                        next[j] = gene;                    
                        if(wordList_set.find(next) != wordList_set.end() && visited.find(next) == wordList_set.end()){
                            que.push(next);                            
                            visited.insert(next);
                        }                        
                    }
                }                
            } 
            step++;
        }     
        return 0;
    }
};