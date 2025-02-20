class Solution {
public:

    int longestOnes(vector<int>& nums, int k) {
        int left = 0,right = 0;
		int maxCount = 0,zeroCount = 0;
		
		while(right <nums.size())
		{
			if(nums[right] == 0){
				zeroCount++;
			}
			while(zeroCount > k){
				if(nums[left] == 0)
					zeroCount--;
				left++;
			}			
			maxCount = max(maxCount,right - left + 1);	
			right++;			
		}
		return maxCount;
    }


    int longestOnes_(vector<int>& nums, int k) {
        int left = 0,right = 0;
		int maxCount = 0;
		queue<int> q;
		while(right <nums.size())
		{
			if(nums[right] == 0){
				//把0放置queue
				q.push(right);				
				if(q.size() > k){
					//left 移到第一個0的隔壁
					left = q.front() + 1;
					q.pop();
				}				
			}				
			maxCount = max(maxCount,right - left + 1);	
			right++;			
		}
		return maxCount;
    }
	

	
};