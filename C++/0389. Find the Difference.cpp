#include<string>


using namespace std;
class Solution {
public:

    char findTheDifference(string s, string t) {
        int n = 0;
        for(int i = 0;i < s.length();i++){            
            n ^= s[i];   
            n ^= t[i];      
        }
        n ^= t[s.length()];      
        return n;
    }
};