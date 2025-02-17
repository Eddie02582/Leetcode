class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        long first = LONG_MAX, second = LONG_MAX;
        
        for (int num : nums) {
            if (num <= first) {
                first = num;  // 更新最小值
            } else if (num <= second) {
                second = num;  // 更新次小值
            } else {
                return true;  // 找到第三個符合條件的數字
            }
        }
        
        return false;  // 若遍歷完都沒有找到三元組
    }
};
