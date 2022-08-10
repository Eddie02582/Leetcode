class Solution {
public:
    string removeKdigits(string num, int k) {
		if (k > num.size())
			return "0";
        vector<int> stack;   
        string ans = "";
        for(auto &c : num){
            int n = c -'0';
            while(k > 0 && !stack.empty() && n < stack[stack.size() -1]){
                stack.pop_back();
                k --;
            }
			if(stack.empty() && n == 0)
				continue;
            stack.push_back(n);
        }
        int end =  k > 0 ? stack.size() - k:stack.size();
        for(int i = 0;i < end;i++){    
            ans += to_string(stack[i]);
        }       
        return ans == "" ? "0":ans;
    }
};