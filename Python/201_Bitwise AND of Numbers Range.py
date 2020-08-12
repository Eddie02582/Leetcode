class Solution:
    def rangeBitwiseAnd(self, m, n):           
        ans = 0
        for i in range(31,-1,-1):  
            dm =  m & (1 << i) 
            dn =  n &(1 << i)
            if dm != dn:
                return ans
            elif dm and dn:
                ans += 1 << i  
        
        return ans




sol = Solution()
sol.rangeBitwiseAnd(5,7)