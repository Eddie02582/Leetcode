class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> index;
        int ret = 0;
        for(int i =0;i<s.size();++i){
			//如果是( 或是空的需要push
            if(s[i]=='(' || index.empty()){
                index.push(i);
            }
            else{
				//如果是),需要檢查棧頂元素是否能匹配
                if(s[index.top()] == '('){
                    index.pop();
					//如果棧是空的,表示到i之前全部匹配,此時長度為i + 1;
					//如果棧不是空的,i - 最後一個沒匹配的
                    ret = max(ret,index.empty()? i+1:i-index.top());
				}				
                else{
                    index.push(i);
                }
            }
        }
        return ret;

    }
	
	
};