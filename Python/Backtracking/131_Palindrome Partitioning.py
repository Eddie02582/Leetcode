import copy
class Solution(object):
    res = []
    def partition(self, s): 
        self.res = []
        if s == '':
            return self.res
        self.dfs(s,[],0) 
        return self.res
    
    def dfs (self,s,remain,left):      
        if left == len(s):
            self.res.append(copy.deepcopy(remain))
            return 
        
        for right in range(left,len(s)):
            if self.isPalindroom(s,left,right):
                remain.append(s[left:right+1])  
                self.dfs(s,remain,right+1)
                remain.pop(-1)
            
    def isPalindroom(self,s,left,right):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
            
        return left>=right
RES = [
  ["aa","b"],
  ["a","a","b"]
]        
        
        
sol =  Solution()

assert sol.partition('aab') == RES