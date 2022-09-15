class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        ios::sync_with_stdio(false); 
        cin.tie(nullptr);
        sort(arr.begin(),arr.end());
        int diff = abs(arr[0] - arr[1]);
        for(int i = 2;i<arr.size();i++){                
            if(abs(arr[i] - arr[i - 1]) != diff ){               
                return false;
            }
        }        
        return true;  
    }
};