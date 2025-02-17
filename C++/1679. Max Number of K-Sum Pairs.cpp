class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sorted(nums.begin(),nums,end());
		int left = 0,right = nums.size() - 1;
		int count = 0;
		while(left < right){
			int sum = nums[left] + nums[right];
			if(sum == k){
				count++;
				left++;
				right--;
			}
			else if(sum > k){
				right--;
			}
			else if(sum < k){
				left++;
			}			
		}
		
		return count;
		
    }
	int maxOperations2(vector<int>& nums, int k) {
		unordered_map<int, int> count;
		int operations = 0;

		for (int num : nums) {
			int complement = k - num;
			
			// 如果 complement 在哈希表中，并且它的计数大于 0
			if (count[complement] > 0) {
				operations++;
				count[complement]--;
			} else {
				count[num]++;
			}
		}

		return operations;
	}
	
	
};