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
#include<vector>
#include<string>
#include<iostream>

using namespace std;
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;

        generate(ans,"",n,n);
        return ans;
    }
    //100% reduce 
    //https://leetcode.com/submissions/detail/567617937/
    void generate(vector<string> &ans,string s,int left,int right){
       
        if(left == 0 & right == 0){
            ans.push_back(s);
            return; 
        }
        if(left > 0)
            generate(ans,s + "(",left - 1,right);  
        if(right > 0 && left < right )
            generate(ans,s + ")",left,right - 1); 
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