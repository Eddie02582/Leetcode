# Letter Combinations of a Phone Number


## 原題目:
```
Given a string containing digits from 2-9 inclusive, return all
 possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) 
is given below. Note that 1 does not map to any letters.

 dict ={
     '2':['a','b','c'],
     '3':['d','e','f'],
     '4':['g','h','i'],
     '5':['j','k','l'],
     '6':['m','n','o'],
     '7':['p','q','r','s'],
     '8':['t','u','v'], 
     '9':['w','x','y','z'],  
 }       


Example:

    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

## 思路 backtracking
使用遞迴每次拆一個digit,並把剩下的digit傳入


## Code

#### C++


```c++
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};  // 边界处理
        unordered_map<char, string> phoneMap{
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
            {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
        };
        vector<string> result;
        string combination;
        backtrack(digits, phoneMap, 0, combination, result);
        return result;
    }

private:
    void backtrack(const string& digits, unordered_map<char, string>& phoneMap, 
                   int index, string& combination, vector<string>& result) {
        if (index == digits.size()) {
            result.push_back(combination);
            return;
        }

        char digit = digits[index];
        string letters = phoneMap[digit];

        for (char letter : letters) {
            combination.push_back(letter);
            backtrack(digits, phoneMap, index + 1, combination, result);
            combination.pop_back();  // 回溯，撤销选择
        }
    }
};










```



類似作法,改成記錄每次digits位置
```python
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {'2':"abc",'3':"def",'4':'ghi','5':'jkl','6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans = []
        def backtracking(word,index):
            if len(word) == len(digits):
                ans.append(word)
                return            
            for letter in mapping[digits[index]]:
                backtracking(word + letter,index + 1)        
        backtracking("",0)   
        return ans
```


     


## 思路 bfs
```
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {"2":"abc","3":"def","4":"ghi",                  
                  "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
                 }        
        from collections import deque    
        
        ans = deque([""])          
        for digit in digits:           
            for _ in range(len(ans)):  
                s = ans.popleft()
                for letter in lookup[digit]:
                    ans.append(s + letter)                      
        return ans if digits else []
```