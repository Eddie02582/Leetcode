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
        que.push(beginWord);         
        int step = 1;
        while (!que.empty()){            
            int size = que.size();
            for(int i = 0; i < size;i++){
                string cur = que.front();
                que.pop();
                if(cur == endWord)
                    return step;
                for (int j = 0;j < cur.size();j++){
                    for(int k = 0;k <26;k++){
                        string next = cur;
                        next[j] =  'a' + k; 
                        if(wordList_set.count(next)){
                            que.push(next);                            
                            wordList_set.erase(next);
                        }
                    }                    
                }               
                 
            } 
            step++;
        }     
        return 0;
    }
};