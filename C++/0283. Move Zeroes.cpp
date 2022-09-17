class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int index = 0;
        for(auto n : nums){
           if(n != 0){
               nums[index++] = n;
           }
        }
        for(int i = index;i < nums.size();i++){
            nums[i] = 0;
        }
        
    }
};