import copy
class Solution:
    def permute_dfs(self, nums):    
        def helper(nums,visited,arr,ret):
            if len(arr) == len(nums):            
                ret.append(copy.copy(arr))            
                return
            for i in range(len(nums)):                
                if visited[i] == 0:
                    arr.append(nums[i])
                    visited[i] = 1
                    helper(nums,visited,arr,ret)
                    visited[i] = 0
                    arr.pop()
                    
        visited = [0] * len(nums)
        ret = []               
        helper(nums,visited,[],ret)
        return ret
    
    def permute(self, nums: List[int]) -> List[List[int]]:             
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
print (sol.permute([1,2,3]))








