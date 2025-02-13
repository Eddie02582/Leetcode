#include<vector>
#include<string>
#include<iostream>

using namespace std;
class Solution {
public:
    void backtrack(string& cur, int left, int right, int n, vector<string>& result) {
        if (cur.size() == 2 * n) {
            result.push_back(cur);
            return;
        }

        if (left < n) {
            cur.push_back('(');
            backtrack(cur, left + 1, right, n, result);
            cur.pop_back();  // 撤销选择
        }

        if (right < left) {
            cur.push_back(')');
            backtrack(cur, left, right + 1, n, result);
            cur.pop_back();  // 撤销选择
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string cur;
        backtrack(cur, 0, 0, n, result);
        return result;
    }
};



int main()
{
    Solution sol;
    sol.generateParenthesis(3);
}


//Input: n = 3
//Output: ["((()))","(()())","(())()","()(())","()()()"]