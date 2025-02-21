class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> ret;
        
        for (int  n : asteroids) {           		
			if (ret.empty()){
                ret.push_back(n);  				
            } 
			else if ( n >0){
                ret.push_back(n);  				
            } 
			else{
				//栈裡面是正
				while(!ret.empty() && ret.back() > 0 && abs(ret.back()) <abs(n) )
					ret.pop_back();
					
                if (ret.empty() || ret.back() < 0) {
                    ret.push_back(n);
                }
				// 如果栈顶小行星与当前小行星大小相同，两者都消失
                else if (abs(ret.back()) == abs(n)) {
                    ret.pop_back();
                }				
			
			}
		}
		return ret;
    }
};
