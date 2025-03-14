class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> indexs;		
		int n = temperatures.size();
        vector<int> ret(n,0);
		for(int i = 0;i<n;++i){
			while(!indexs.empty() && temperatures[indexs.top()] < temperatures[i]){
				ret[indexs.top()] = i - indexs.top();
				indexs.pop();
			}
			indexs.push(i);
			
		}
		return ret;
    }
};
