import copy
class Solution:
    def permute_backtracking(self, nums):        
        def backtracking(array,visited):
            if len(array) == len(nums):
                res.append(array[:])
                return         
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    backtracking(array + [nums[i]],visited)
                    visited[i] = False

        visited = [False] * len(nums)        
        res = []
        backtracking([],visited)
        return res
    
    def permute(self, nums):             
        if len(nums) == 0: 
            return []
            
        if len(nums) == 1: 
            return [nums] 
            
        ret = []# empty list that will store current permutation   
      
        # Iterate the input(lst) and calculate the permutation 
        for i in range(len(nums)): 
            m = nums[i] 
      
           # Extract lst[i] or m from the list.  remLst is 
           # remaining list 
            remLst = nums[:i] + nums[i+1:] 
            
           # Generating all permutations where m is first 
           # element 
            for p in self.permute(remLst): 
                ret.append([m] + p) 
        return ret 
      


sol =Solution()
print (sol.permute([1,2,3,4]))








