
#include <unordered_map>
#include <vector>
#include <string>
using namespace std;


class Solution {
public:
       vector<int> findSubstring(string s, vector<string>& words) {
        int step = words[0].size();
        if(words.size() * step > s.size())
            return vector<int>();
            
        unordered_map<string,int> match;
		vector<int> ans;
		
		for(auto word:words)			
			match[word]++;				
		
		for (int i = 0;i <= s.size() - step * words.size() ;i++){	
			int matchCnt = 0;   
			unordered_map<string,int> slide;	
			for (int j = 0;j< words.size();j++)
			{                
				string word = s.substr(i + j*step,step);                
				if(match.find(word) == match.end())
					break;		
				slide[word]++;										
				if(slide[word] == match[word])
					matchCnt++;
				else if  (slide[word] > match[word]){
					matchCnt--;			
                }
			}
			if (match.size() == matchCnt)
				ans.push_back(i);
		}
		return ans;  
    }

};

int main (){
	Solution sol;
	string s = "barfoothefoobarman";
	vector<string>words = {"foo","bar"};
	sol.findSubstring(s,words);

	return 0;
}