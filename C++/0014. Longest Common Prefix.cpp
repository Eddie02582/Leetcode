#include <vector>
#include<string>
#include<algorithm>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 1)
            return strs[0];
        sort(strs.begin(),strs.end());       
        string prefix = "";
        int size = strs.size();
        for (int i = 0; i < strs[0].size() & i < strs[size - 1].size() ;i++ ){           
            if(strs[0][i] != strs[size -1][i])
                return prefix;
            
            prefix += strs[0][i];  
        }
        return prefix;

    }
};




