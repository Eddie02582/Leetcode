class Solution {
public:    
    int bagOfTokensScore(vector<int>& tokens, int power) {        
        sort(tokens.begin(),tokens.end());
        int left = 0,right = tokens.size() - 1;        
        int max_score = 0;
        int score = 0;
        while (left <= right){            
            
            if(power >= tokens[left]){
                score++;
                power -=tokens[left++];               
            }
            else{
                if(score == 0){
                    break;
                }
                power +=tokens[right--];
                score--;                
            }  
            if(score> max_score)
                max_score = score;   
        }  
        return max_score;
    }    
};
