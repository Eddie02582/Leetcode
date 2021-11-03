class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        
        int closest = nums[0] + nums[1] + nums[2];
        
        for (int i = 0;i<nums.size() - 2;i++){
            int left = i + 1,right = nums.size() - 1;            
            while (left < right){
                int total = nums[left] + nums[right] + nums[i];                
                if (total < target) 
                    left += 1;    
                else if (total > target) 
                    right -= 1;                  
                else
                    return target;            
  
                
                if(abs(target - total) < abs(target - closest))                     
                    closest = total;    
            }            
        }
        return closest;
    }
};