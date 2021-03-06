class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []        
        
        def backtracking(sol,start,n):
            if len(sol) == 4 and n == 0:
                ans.append('.'.join(sol))
                return 
            elif len(sol) == 4 or n == 0:
                return
            if n >= 1:
                val = s[start]
                backtracking(sol + [val] ,start + 1, n - 1)
            if n >= 2 and s[start] != '0':
                val = s[start : start + 2]
                backtracking(sol + [val],start + 2, n - 2)          
            if n >= 3 and s[start] != '0':
                val = s[start :start + 3]
                if int(val) <= 255:
                    backtracking(sol + [val] ,start + 3, n - 3)
        
        backtracking([],0,len(s))
        
        return ans     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''