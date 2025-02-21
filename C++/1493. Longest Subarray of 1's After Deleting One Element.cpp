class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left = 0,right = 0;
		int longest = 0;
		int zeroCount = 0;
		
		while(right < nums.size()){			
			if(nums[right] == 0){
				zeroCount ++;				
			}			
			while(zeroCount > 1){
				if(nums[left]==0)
					zeroCount--;
				left++;
			}		
			//因為一定要砍掉1個
			//假設至少有一個0=> right -left(扣掉1個0)
		    //如果全部都1    => right -left(扣掉1個1),left - 0,right = nums.size() - 1
			longest = max(longest,right - left);
			right++;
		}				
		return longest;	
    }
	int longestSubarray_2(vector<int>& nums) {
        int left = 0,right = 0;
		int longest = 0;
		int zeroCount = 0;
		int n = nums.size();
		
		while(right < n){			
			if(nums[right] == 0){
				zeroCount ++;				
			}			
			while(zeroCount > 1){
				if(nums[left]==0)
					zeroCount--;
				left++;
			}			
			longest = max(longest,right - left + 1 - zeroCount);
			right++;
		}	
		return longest == n ? longest - 1:longest; 	
    }
	
};