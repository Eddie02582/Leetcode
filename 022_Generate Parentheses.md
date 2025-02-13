# Generate Parentheses

## 原題目:
```
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

## 思路
dfs/backtracking問題,判斷條件,當left或right大於n時,或right 大於left,當left ==n 和 right ==n時即為答案(left 大於right前面以判斷)

## Code

#### Python

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtracking(left,right,s):
            if left > n or right > n or right > left:
                return            
            if left == n and right == n:
                res.append(s)
                return
           
            backtracking(left + 1,right,s + "(")           
            backtracking(left ,right + 1 ,s + ")")
        
        backtracking(0,0,'')
        
        return res
        
```
#### C-sharp

```csharp
public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        IList<string> ans = new List<string>();
        generateParenthesis(n,n,"",ans);
        return ans;
    }

    public void generateParenthesis(int l,int r,string s,IList<string> ans) {
        if ( l > r ){
            return ;
        }
        if (l == 0 && r == 0)
            ans.Add(s);   
        if (l > 0)     
            generateParenthesis(l - 1,r ,s + "(",ans);
        if (r > 0)
            generateParenthesis(l ,r - 1 ,s + ")",ans);            

    }

}
```


#### c++

```c++
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
            cur.pop_back();  
        }

        if (right < left) {
            cur.push_back(')');
            backtrack(cur, left, right + 1, n, result);
            cur.pop_back();  
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string cur;
        backtrack(cur, 0, 0, n, result);
        return result;
    }
};
```


比較簡潔但是可能內存多一點,不使用push_back,string &cur=>string cur
```c++
#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    void backtrack(string cur, int left, int right, int n, vector<string>& result) {
        // 终止条件：括号组合长度达到 2n
        if (cur.size() == 2 * n) {
            result.push_back(cur);
            return;
        }

        // 选择放置 '('
        if (left < n) {
            backtrack(cur + "(", left + 1, right, n, result);
        }

        // 选择放置 ')'
        if (right < left) {
            backtrack(cur + ")", left, right + 1, n, result);
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> result;
        backtrack("", 0, 0, n, result);
        return result;
    }
};
```







## 思路 BFS 
類似BFS 思路,只是加了判斷
```csharp

class Queue{
        public string s = "";
        public int l  = 0;
        public int r = 0;
}

public class Solution {
    public IList<string> GenerateParenthesis(int n)
    {
        IList<string> ans = new List<string>();
        List<Queue> queues = new List<Queue>();
        queues.Add(new Queue { l = n, r = n, s = "" });
        while (queues.Count()> 0)
        {
            Queue queue = queues[0];
            queues.RemoveAt(0);
            if (queue.l == 0 && queue.r == 0)
                ans.Add(queue.s);
            if (queue.l <= queue.r)
            {
                if (queue.l > 0)              
                    queues.Add(new Queue { l = queue.l - 1, r = queue.r, s = queue.s + "(" });                
                if (queue.r > 0)               
                    queues.Add(new Queue { l = queue.l, r = queue.r - 1, s = queue.s + ")" });
                
            }
        }
        return ans;
    }   

}
```