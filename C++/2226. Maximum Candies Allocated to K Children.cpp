class Solution {
public:
    // 辅助函数：判断是否可以将 maxCandies 个糖果分配给至少 k 个孩子
    bool canAllocate(vector<int>& candies, long long k, int maxCandies) {
        long long matchPiles = 0;
        for (auto candy : candies) {
            matchPiles += (long long)candy / maxCandies;  // 计算每个孩子能获得的糖果数
            if (matchPiles >= k) {
                return true;  // 如果已足够分配给 k 个孩子，返回 true
            }
        }
        return false;
    }

    int maximumCandies(vector<int>& candies, long long k) {
        int left = 1, right = *max_element(candies.begin(), candies.end());  // 查找的范围从 1 到 candies 数组的最大值
        int result = 0;

        // 二分查找：找出最大可以分配给孩子的糖果数
        while (left <= right) {
            int mid = (left + right) / 2;  // 计算中间值
            if (canAllocate(candies, k, mid)) {
                result = mid;  // 能分配给 k 个孩子时更新结果
                left = mid + 1;  // 尝试更多的糖果数
            } else {
                right = mid - 1;  // 如果不能分配给 k 个孩子，减少糖果数
            }
        }

        return result;
    }
};