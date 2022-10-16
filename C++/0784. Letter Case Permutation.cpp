class Solution {
public:
    vector<string> letterCasePermutation(string s) {        
        vector<string> ans;
        vector<string> permutations{{""}};
        
        for(auto &c :s){          
            vector<char> letters {c};
            if( c-'a'>=0 && c -'a' <=26){
                letters.push_back(toupper(c));
            }
            else if( c-'A'>=0 && c -'A' <=26){
                letters.push_back(tolower(c));
            }    
            vector<string> temp;
            for(auto &letter :letters){
                for(auto &permutation :permutations){                    
                    temp.push_back(permutation+letter);
                }
            }           
            permutations = temp;
        }
        return permutations;
    }
};