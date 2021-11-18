#include<vector>
#include<unordered_set>

using namespace std;


class Solution {
public:

    string findDifferentBinaryString(vector<string>& nums) {
        string ans="";
        int i=0;
        for (int i = 0;i<nums.size();i++){
            ans += nums[i][i] == '1' ? '0':'1';
        }     
        return ans;
    }
};