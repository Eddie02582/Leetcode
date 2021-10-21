#includes<vector>
#includes<unordered_set>

using namespace std;
class Solution {
public:

    vector<int> findErrorNums(vector<int>& nums) {
        unordered_set <int> exist; 
        int loss = 0;
        int duplicate = 0;
        for (int i = 0;i < nums.size();i++){    
            if(exist.count(nums[i]))
            {
                duplicate = nums[i];
            }
            exist.insert(nums[i]);    
        }
        for (int i = 1;i < nums.size() + 1;i++){    
            if(!exist.count(i))
            {
                loss = i;
                break;
            }
        }        
        return vector<int>{duplicate,loss}; 
    }

    vector<int> findErrorNums(vector<int>& nums) {
        unordered_set <int> exist;      
        int loss = 0;
        int duplicate = 0;
        
        for (int i = 0;i < nums.size();i++){             
            loss += (i + 1);
            if(exist.count(nums[i]))      
                duplicate = nums[i];     
            else
                loss -= nums[i];              
            exist.insert(nums[i]);           
        }        
        
        return vector<int>{duplicate,loss}; 
    }
    
    

    
};















1