class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0];
        int temp = nums[0];
        
        for(int i = 1;i < nums.size();i++){
            temp += nums[i];
            if(temp < nums[i])
                temp = nums[i];
            if(temp > ans)
                ans = temp;            
        }
        
        return ans;  
    }     
};


