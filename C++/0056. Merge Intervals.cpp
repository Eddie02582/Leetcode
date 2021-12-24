class Solution {
public:    
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> ans;
        for (int i = 0; i < intervals.size(); i ++) {           
            if (ans.empty() || intervals[i][0] > ans.back()[1])
                ans.push_back(intervals[i]);
            else if (ans.back()[1] <  y = intervals[i][1])
                ans.back()[1] = y;
        }
        return ans;
    }
    vector<vector<int>> merge_slow(vector<vector<int>>& intervals) {
         vector<vector<int>> ans;
         sort(intervals.begin(), intervals.end());
        
         for (auto &interval: intervals){            
             if(ans.empty() || ans.back()[1] < interval[0])                 
                 ans.push_back(interval);             
             else if (ans.back()[1] < interval[1])   
                ans.back()[1] = interval[1];                 
         }
         return ans;
    }
    
};

