class Solution {
public:
    int findDuplicate_index_sort(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            // 交換目前元素，直到它放到正確的位置
            while (nums[i] != i + 1) {
                if (nums[i] == nums[nums[i] - 1]) {
                    return nums[i];  // 如果目前位置的元素和它的目標位置元素相等，表示重複
                }
                swap(nums[i], nums[nums[i] - 1]);
            }
        }
        
        return -1;  // 不会到达这里，因为题目保证存在重复数字
    }
    int findDuplicate(vector<int>& nums) {
        for (int num : nums) {
            int idx = abs(num) - 1;
            if (nums[idx] < 0) {
                return abs(num);
            }
            nums[idx] *= -1;
        }
        return -1;
    }

	
	
	//當成linklist的概念
    int findDuplicate(vector<int>& nums) {
        int slow = 0, fast = 0;
        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast) {
                break;
            }
        }

        int slow2 = 0;
        while (true) {
            slow = nums[slow];
            slow2 = nums[slow2];
            if (slow == slow2) {
                return slow;
            }
        }
    }
	
};