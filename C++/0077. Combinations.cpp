class Solution {
public:
    vector<vector<int>> combination;
    vector<vector<int>> combine(int n, int k) {         
        vector<int>path;
        backtracking(k,n,1,path);
        return combination;
    }  
    void backtracking(int k,int n,int curr,vector<int>&path){
        if(path.size() == k){
            combination.push_back(path);           
        }
        else if (curr <= n ){
            path.push_back(curr);
            backtracking(k,n,curr + 1,path);
            path.pop_back();
            backtracking(k,n,curr + 1,path);
        }        
    }
};