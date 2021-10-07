#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;

        unordered_map<char,int> imp;  
        for(int i = 0;i < s.size();i++)   
        { 
            imp[s[i]] += 1;    
            imp[t[i]] -= 1;  
        }  
        
        for(auto it = imp.begin();it != imp.end();it++)
        {
            if(it->second != 0)
                return false;
        }
        return true;
    }

    bool isAnagram_2(string s, string t) {
        if(s.length() != t.length())
            return false;

        unordered_map<char,int> imp;  
        for(int i = 0; i < s.length(); i++)
        { 
            imp[s[i]]++;    
            imp[t[i]]--;  
        }  
        //c++ 11
        for(auto x : imp)
        {
            if(x.second != 0)
                return false;
        }
        return true;
    }



    bool isAnagram_3(string s, string t) {
        if (s.size() != t.size())
            return false;

        int arr[256] = {0};       
        for(int i = 0;i<s.size();i++)   
        { 
            arr[s[i]] += 1;    
            arr[t[i]] -= 1;  
        }  
        for(int i = 0; i<256 ; i++){
            if(arr[i]!=0)
                return false;           
        }    
        return true;

    }
};



int main()
{
    Solution sol;
    sol.isAnagram_2("anagram","nagaram");
    sol.isAnagram("rat","car");
}