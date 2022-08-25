class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> letters (26);
        
        for (auto c : magazine){
            letters[c - 'a']++;
        }
        for (auto c : ransomNote){
            letters[c - 'a']--;
            if(letters[c - 'a'] < 0)
                return false;
        }          
        
        return true;
                    
    }
};