class Solution {
public:
    string removeStars(string s) {
        vector<char> characters;
        string ret;    
        for (auto c : s) {
            if (c != '*') {
                characters.push_back(c);
            } else {
                characters.pop_back();
            }
        }
		ret.reserve(characters.size());  // 预先分配空间，避免频繁扩容
        // 将结果构建成字符串
        ret.assign(characters.begin(), characters.end());
        
        return ret;
    }
	//都是O(n)但是執行速度比較慢
    string removeStars2(string s) {      
        string ret;        
        ret.reserve(s.size());
        for (auto c : s) {
            if (c != '*') {
                ret.push_back(c);
            } else {
                ret.pop_back();
            }
        }	
        return ret;
    }
	
};
