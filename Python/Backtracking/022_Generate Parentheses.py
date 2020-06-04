class Solution:
    def generateParenthesis(self,n):
        res = []         
        self.helper(n ,n,"",res)        
        return res
        
    def helper(self,left,right,out,res):
        if left < 0 or right < 0 or left > right:
            return 
        if left == 0 and right == 0 :
            res.append(out)
            return 
        self.helper(left - 1, right, out + "(", res)
        self.helper(left, right - 1, out + ")", res)  


    def generateParenthesis_backtrack(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(combine):            
            if combine.count(')') > combine.count('(') or combine.count('(') > n:
                return 
            elif len(combine) == 2 * n:
                res.append(combine[:])
                return []
            for  parenthese in ['(',")"]:
                backtrack(combine + parenthese)

        if n == 0:
            return []

        res = []
        backtrack('')
        return res    



result = [
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

sol = Solution()
assert sol.generateParenthesis(3) == result


