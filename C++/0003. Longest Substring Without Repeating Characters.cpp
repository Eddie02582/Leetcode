class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0,right = 0;
        int longestLength = 0;
        unordered_set<char> char_set;
        
        while(right < s.size()){
            if(char_set.count(s[right])){
                while(s[left] != s[right]){
                    char_set.erase(s[left]);
                    left++;
                }
                left++;
            }           
            char_set.insert(s[right]);            
            longestLength = max(longestLength,right - left + 1);
            right++;
        }
        return longestLength;
    }
    
    int lengthOfLongestSubstring_map(string s) {
        int left = 0,right = 0;
        int longestLength = 0;
        unordered_map<char,int> char_map;
        
        while(right < s.size()){
            if (char_map.count(s[right]) && char_map[s[right]] >=left){
                left = char_map[s[right]] + 1;
            }      
            char_map[s[right]] = right ;         
            longestLength = max(longestLength,right - left + 1);
            right++;
        }
        return longestLength;
    }    
    
};





