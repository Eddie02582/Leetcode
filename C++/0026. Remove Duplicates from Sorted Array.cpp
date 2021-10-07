// Your First C++ Program

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        if (nums.empty())
            return 0;        

        int index = 0;
        for (int i = 1;i < nums.size();i++)
        {
            if (nums[i] != nums[i - 1])
            {
                index += 1;
                nums[index] = nums[i]; 
            }
        }   
        return index + 1;
    }

    int removeDuplicates_2(vector<int>& nums) {

        if (nums.empty())
            return 0;        

        int index = 0;
        for (int i = 0;i < nums.size();i++)
        {
            if (i == 0 || nums[i] != nums[i - 1])
            {                
                nums[index] = nums[i]; 
                index += 1;
            }
        }        

        return index;
    }

    int removeDuplicates_2(vector<int>& nums) {

        if (nums.empty())
            return 0;        

        int index = 0;
        for (int i = 0;i < nums.size();i++)
        {
            if (nums[i] != nums[index])
            {          
                index += 1;      
                nums[index] = nums[i];                
            }
        }  
        return index + 1;
    }


};


int main() {
    vector<int> nums({0,0,1,1,1,2,2,3,3,4 });
	Solution sol;
	sol.removeDuplicates(nums);
}