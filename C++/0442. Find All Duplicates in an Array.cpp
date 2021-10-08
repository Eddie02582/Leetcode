
#include <vector>
#include<string>
#include<set>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        set <int> visited;
        vector <int> duplicates;
        for (int i = 0;i<nums.size();i++){            
            if(visited.count(nums[i]))
                duplicates.push_back(nums[i]);   
            visited.insert(nums[i]);
        }        
        return duplicates;
        
    }
    
    vector<int> findDuplicates_(vector<int>& nums) {       
        vector <int> duplicates;
        for (int i = 0;i<nums.size();i++){  
            if (nums[abs(nums[i]) - 1] < 0)
                duplicates.push_back(abs(nums[i]));
            else
                nums[abs(nums[i]) - 1] *= -1;   
        }        
        return duplicates;
        
    }
};