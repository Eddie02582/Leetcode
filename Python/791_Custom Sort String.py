class Solution:
    def customSortString(self, S: str, T: str) -> str:
        count = {}
        ans,res = "",""
        exist = set(S)
        for t in T:
            if t in exist:
                count[t] = count.get(t,0) + 1
            else:
                res += t          
        for s in S:
            ans += count.get(s,0) * s
            count[s] = 0
        
        ans = ans + res
        
        return ans