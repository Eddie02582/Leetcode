# Substring with Concatenation of All Words

## 原題目:
```
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.
 

Example 1:
	Input: s = "barfoothefoobarman", words = ["foo","bar"]
	Output: [0,9]
	Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
	The output order does not matter, returning [9,0] is fine too.

Example 2:
	Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
	Output: []
	
Example 3:
	Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
	Output: [6,9,12] 

Constraints:
	1 <= s.length <= 104
	1 <= words.length <= 5000
	1 <= words[i].length <= 30
	s and words[i] consist of lowercase English letters.
```

## 思路滑動窗口


## Code


#### c++

```python

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
```




