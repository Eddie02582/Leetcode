#include<vector>
#include<string>
#include<iostream>

using namespace std;
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;

        generate(ans,"",n,n);
        return ans;
    }

    void generate_(vector<string> &ans,string s,int left,int right){
       
        if(left == 0 & right == 0){
            ans.push_back(s);
            return; 
        }
        if (left > right || left < 0 || right < 0)
            return;                   
        generate(ans,s + "(",left - 1,right);  
        generate(ans,s + ")",left,right - 1);    
    }

    //100% reduce 
    //https://leetcode.com/submissions/detail/567617937/
    void generate(vector<string> &ans,string s,int left,int right){
       
        if(left == 0 & right == 0){
            ans.push_back(s);
            return; 
        }
        if(left > 0)
            generate(ans,s + "(",left - 1,right);  
        if(right > 0 && left < right )
            generate(ans,s + ")",left,right - 1); 
    }


};



int main()
{
    Solution sol;
    sol.generateParenthesis(3);
}


//Input: n = 3
//Output: ["((()))","(()())","(())()","()(())","()()()"]