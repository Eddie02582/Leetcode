# Letter Case Permutation


## 原題目:
```
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output  in any order.

 

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]
```

## 思路backtracking

#### Python
``` python
class Solution:
    def letterCasePermutation(self, S):
        ans,n = [],len(S)        
        def backtracking(i,sol):
            if i == n:
                ans.append(sol)
                return
                      
            s_set = set([S[i].lower(),S[i].upper()])  
            for s in s_set:          
                backtracking(i + 1,sol + s)
                    
        backtracking(0,"")
        return ans     
``` 

## 思路iterator



``` python
class Solution:
    def letterCasePermutation(self, S):       
        #bfs
        ans = [""]
        
        for i in range(len(S)):            
            s_set = set([S[i].lower(),S[i].upper()])  
            n = len(ans)
            while n > 0:
                sol = ans.pop(0)
                for s in s_set:
                    ans.append(sol + s)                   
                n -= 1            
        return ans     
``` 







