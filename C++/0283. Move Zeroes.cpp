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
	
    void moveZeroes2(vector<int>& nums) {
        int write = 0;

        for (int read = 0; read < nums.size(); read++) {
            if (nums[read] != 0) {
                swap(nums[read], nums[write]);
                write++;
            }
        }        
    }
};