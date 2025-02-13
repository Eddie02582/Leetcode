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