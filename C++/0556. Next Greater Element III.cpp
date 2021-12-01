#include<vector>
#include<stack>
#include<unordered_map>
#include<algorithm>
using namespace std;

class Solution {
public:
    int nextGreaterElement(int n) {
        stack<int> st;
        vector<int> nums;
        //change n to vector (reverse)
        while (n){            
            nums.push_back(n %10);  
            n /= 10;
        }     

        int index = -1,index2 = -1;

        //find first index change
        for(int i = 0; i < nums.size() ;i++){       
            if(!st.empty() && nums[i] < nums[st.top()]){
                index = i;
                break;     
            }
            st.push(i);
        }  

        if(index == index2)
            return -1;

        //find second second change
        while (!st.empty() && nums[index] < nums[st.top()] )
        {
            index2 = st.top();
            st.pop();
        }

        
        swap(nums[index],nums[index2]);   

        //sort 0 to index - 1     
        sort(nums.begin(),nums.begin() + index,greater<int>());


        //vector to n
        long next_greater = 0;
        for(int i = nums.size()- 1; i >=0;i--){          
            next_greater = next_greater *10 + nums[i];
        }
       

        return next_greater > INT_MAX? -1:next_greater;

    }
};

int main(){

    Solution sol;
    int n = 2147483476;
    sol.nextGreaterElement(n);
    return 0;
}