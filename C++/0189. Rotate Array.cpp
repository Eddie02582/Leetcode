class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int m = nums.size();
        k = k % m;
        vector<int>temps(m);
        for(int i = 0;i<m;i++){
            temps[(i + k)%m] = nums[i];
        }
        for(int i = 0;i<m;i++){
            nums[i] = temps[i];
        }     
    }
};