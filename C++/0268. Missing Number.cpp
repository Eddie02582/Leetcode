#include <set>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        set<int> numbers(nums.begin(),nums.end());
        for (int i = 0;i < nums.size();i++){            
            if(numbers.count(i) == 0 )
                return i;          
        }        
        return nums.size();         
    }

    int missingNumber_2(vector<int>& nums) {
        int ans = 0;
        for (int i = 0;i < nums.size();i++){            
            ans ^= nums[i];         
        }        
        for (int i = 0;i <= nums.size();i++){ 
            ans ^= i; 
        }        
        return ans;         
    }

    int missingNumber_3(vector<int>& nums) {
        int ans = 0;
        for (int i = 0;i <= nums.size();i++){ 
            ans += i; 
        }   
        for (int i = 0;i < nums.size();i++){            
            ans -= nums[i];         
        }        
     
        return ans;         
    }

};



int main(void)
{
    Solution sol;
    vector<int> nums {3,0,1};
    sol.missingNumber(nums);
}

//nums = [3,0,1]
//2

//nums = [0,1]
//2



//nums = [9,6,4,2,3,5,7,0,1]
//8