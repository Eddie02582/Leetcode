class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int total_sum = 0, left_sum = 0;
        int n = nums.size();
        
        // 计算总和
        for (int num : nums) {
            total_sum += num;
        }

        // 遍历数组，边计算左边和
        for (int i = 0; i < n; ++i) {
            // 右边和 = 总和 - 左边和 - 当前元素
            if (left_sum == total_sum - left_sum - nums[i]) {
                return i;
            }
            left_sum += nums[i]; // 更新左边和
        }
        
        return -1; // 没有找到中心索引
    }
};
