#include<unordered_map>

using namespace std;
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
		int ret = 0;
		
		for(int num:nums){
			// 如果 num-1 不在 numSet 中，说明 num 是一个序列的起点
			if(!numSet.count(num - 1)){
				int curr = num;
				while(numSet.count(curr)){					
					curr++;
				}
				ret = max(ret,curr - num);
			}			
		}
		return ret;
    }
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> h;
        int ans = 0;
        for (int num : nums) {
            if (h.count(num)) continue;
            
            auto it_l = h.find(num - 1);
            auto it_r = h.find(num + 1);
            
            int l = it_l != h.end() ? it_l->second : 0;
            int r = it_r != h.end() ? it_r->second : 0;
            int t = l + r + 1;
            
            h[num] = h[num - l] = h[num + r] = t;
            
            ans = max(ans, t);            
        }
        
        return ans;
    }
};