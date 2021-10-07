// Your First C++ Program

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>  
#include <unordered_map> 
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        sort(nums.begin(), nums.end());
        for(int i = 1; i < nums.size(); i++)
        {
            if(nums[i-1] == nums[i])
                return true;
        }
        return false;        
    }

    bool containsDuplicate_2(vector<int>& nums) {
        
        set<int> exist;         
        for (int i = 0;i<nums.size();i++){             
            if (exist.count(nums[i]))           
                return true;            
            exist.insert(nums[i]);
        }        
        return false;        
    }
};



int main() {
	//int arr[] = {1,1,1,3,3,4,3,2,4,2 };
	//vector<int> nums(arr,arr+10);
    vector<int> nums({1,1,1,3,3,4,3,2,4,2 });


	Solution sol;
	sol.containsDuplicate(nums);
}