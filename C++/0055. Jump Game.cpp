#include <vector>
#include <iostream>
#include <unordered_map>
#include <stack>
using namespace std;


class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        for(int i = 1; i<n;i++){
            if(i > nums[i-1]) return false;
            nums[i] = max( nums[i-1], i + nums[i] );
        }
        return true;
    }  
    bool canJump_(vector<int>& nums) {  
        int max_loc = 0;
        for(int i = 0; i <nums.size();i++){
            if (i > max_loc) 
                return false; 
            else
                max_loc = max(i + nums[i],max_loc);
            if (max_loc >= nums.size() - 1) 
                return true;
        }
        return true;
    }
    }
};


int main(){
    
    vector<int> nums1{2,3,1,1,4};   
    Solution sol;
    sol.canJump(nums1);
    
}