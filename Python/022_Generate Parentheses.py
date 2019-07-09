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

result = [
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

sol = Solution()
assert sol.generateParenthesis(3) == result