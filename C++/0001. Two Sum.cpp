// Your First C++ Program

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> lookup;   
        for (int i = 0; i < nums.size(); i++)
        {
            int n = target - nums[i];
            if(lookup.count(n))
                return { lookup[n], i};
            lookup[nums[i]] = i;        
        }
        return {};           
    }
    vector<int> twoSum_2(vector<int>& nums, int target) {
        unordered_map<int,int> lookup;   
        for (int i = 0; i < nums.size(); i++)
        {
            int n = target - nums[i];
            if (lookup.find(n) != lookup.end()) 
                return { lookup[n], i};
            lookup[nums[i]] = i;        
        }
        return {};          
    }

    vector<int> twoSum_3(vector<int>& nums, int target) {
        unordered_map<int, int> imap;
        
        for (int i = 0;; ++i) {
            auto it = imap.find(target - nums[i]);
            
            if (it != imap.end()) 
                return vector<int> {i, it->second};
                
            imap[nums[i]] = i;
    }

};


int main() {

    int target = 9;
    vector<int> nums({2,7,11,15});
	Solution sol;
	sol.twoSum(nums,target);
}