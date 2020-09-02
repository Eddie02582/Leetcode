class Solution:
    def letterCasePermutation_backtracking(self, S):
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
sol =   Solution()     
sol.letterCasePermutation("a1b2")
        
        
        