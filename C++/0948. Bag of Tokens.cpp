class Solution {
public:
    int max_score = 0;
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int size = tokens.size();  
        vector<bool> visited(size);    
        backtracking(tokens,visited,power,0,0);
        return max_score;
    }
    void backtracking(vector<int>& tokens, vector<bool> &visited,int power,int score = 0,int v = 0){
        int size = tokens.size();            
        if(score > max_score)
            max_score = score;               
        if (v == size)
            return ;

        for(int i = 0;i < size ;i++){
            auto token = tokens[i];            
            if(!visited[i]){                         
                visited[i] = true;
                if (power >= token){
                    backtracking(tokens,visited,power - token,score + 1,v  + 1);
                }
                else if (score >= 1){                
                    backtracking(tokens,visited,power + token,score - 1,v + 1);
                }                
                visited[i] = false; 
            }              
        }
        
        
    }    
    
};
