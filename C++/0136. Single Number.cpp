class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int n = 0;
        for(auto num :nums)
            n ^= num;
        return n;
        
    }
};