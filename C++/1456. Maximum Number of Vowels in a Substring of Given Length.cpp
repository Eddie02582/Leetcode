class Solution {
public:
    int maxVowels(string s, int k) {
		int len = s.size();
		unordered_set<char> vowels = { 'a', 'e', 'i', 'o','u' };	
		int result = 0;
		int currVowels = 0;
		int left = 0,right = 0;
		
		
		while(right < len){
			
			currVowels += vowels.count(s[right]);
			if (right - left +1 > k){          
				currVowels -= vowels.count(s[left]);                       
				left++;
			}
            result = max(currVowels,result);
			right++;			
		}		
		return result;
    }
};