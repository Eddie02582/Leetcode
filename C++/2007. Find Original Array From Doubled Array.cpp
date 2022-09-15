class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        sort(changed.begin(),changed.end());
        unordered_map<int,int> counts;
        vector<int> ans ;
        for(auto n : changed){
            counts[n]++;
        }
        
        for(auto n : changed){
            if(counts[n] > 0){                   
                counts[n]--;
                counts[2 * n] --;
                ans.push_back(n);
                if(counts[2 * n] < 0)
                    return vector<int>{};
                
            }        
        }        
        return ans;    
    }
};