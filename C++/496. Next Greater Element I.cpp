#include <vector>
#include <iostream>
#include <unordered_map>
#include <stack>
using namespace std;


class Solution {
public:
    //O(M*N)
    vector<int> nextGreaterElement_(vector<int>& nums1, vector<int>& nums2) {
        vector<int>ans(nums1.size() ,-1);
        for (int i = 0;i< nums1.size();i++){
            bool bfind = false;
            for (int j = 0;j < nums2.size();j++){
                if(nums1[i] == nums2[j])
                    bfind = true;                    
                    
                if(bfind && nums2[j] > nums1[i]){                   
                    ans[i] = nums2[j];
                    break;
                }

            }
        }
        
        return ans;
    }

    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int>ans(nums1.size() ,-1);
        stack<int>s;
        unordered_map <int,int> loc;
        for (int i = 0;i< nums1.size();i++){
            loc[nums1[i]] = i;
        }       
        for (int j = 0;j < nums2.size();j++){
            while(!s.empty() && s.top() < nums2[j]){
                if(loc.count(s.top())){
                    ans[loc[s.top()]] = nums2[j];
                    s.pop();
                }
                else
                    break;                
            }  
            s.push(nums2[j]);
        }     
        return ans;
    }

    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int>ans(nums1.size() ,-1);
        stack<int>s;
        unordered_map <int,int> loc;
        for (int i = 0;i< nums1.size();i++){
            loc[nums1[i]] = i;
        }       
        for (int j = 0;j < nums2.size();j++){
            while(!s.empty() && s.top() < nums2[j]){
                if(loc.count(s.top())){
                    ans[loc[s.top()]] = nums2[j];
                    s.pop();
                }
                else
                    break;                
            }  
            s.push(nums2[j]);
        }     
        return ans;
    }
};


int main(){
    
    vector<int> nums1{4,1,2};
    vector<int> nums2{1,3,4,2};
    Solution sol;
    sol.nextGreaterElement(nums1,nums2);
    
}