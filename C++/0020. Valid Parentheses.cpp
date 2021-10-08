#include <iostream>
#include <string>
#include <map>  
#include <stack>
using namespace std;
		
class Solution {
public:
    bool isValid(string s) {
        stack<char> brackets;
		
        map<char, char> brackets_pair {
           {')', '('},
           {']', '['},
           {'}', '{'}
        };	

       for(char& c : s) {
           if (brackets.empty() || brackets.top() != brackets_pair[c])
               brackets.push(c);   
           else if (!brackets.empty() && brackets.top() == brackets_pair[c]) 
               brackets.pop();
           else return false;
       }        
        return brackets.empty();
    }
};

int main()
{
	string s = "{[]}";
	Solution sol;
	sol.isValid(s);

}