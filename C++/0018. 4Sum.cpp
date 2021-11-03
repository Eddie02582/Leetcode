class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        if(nums.size() < 4)
            return ans;
        
        sort(nums.begin(),nums.end());
        
        for(int i = 0;i < nums.size() - 3;i++){
            if ( i != 0 && nums[i] == nums[i - 1])
                continue;              
            for(int j = i + 1;j < nums.size() - 2;j++){
                if ( j != i + 1 && nums[j] == nums[j - 1])
                    continue;              
                
                          
                int left = j + 1,right = nums.size() - 1;                
                while (left < right){
                    long total = (long)nums[i] + (long)nums[j] +  (long)nums[left] + (long)nums[right];
                    if(total == target){                        
                        ans.push_back(vector<int>{nums[i],nums[j],nums[left],nums[right]}) ;                       
                        left += 1;
                        right -= 1;
                        
                        while (left < right && nums[left] == nums[left - 1])
                            left += 1;
                        
                        while (left < right && nums[right] == nums[right + 1])
                            right -= 1; 
                        
                    }
                    else if (total > target)
                        right -= 1; 
                    else
                        left += 1;                    
                    
                } 
                
            }
            
        }
        return ans;
        
    }
};