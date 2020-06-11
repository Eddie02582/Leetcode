class Solution:
    def permuteUnique(self, nums):        
        def backtracking(array,visited):
            if len(array) == len(nums):
                res.add(tuple(array[:]))
                return         
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    backtracking(array + [nums[i]],visited)
                    visited[i] = False

        visited = [False] * len(nums)        
        res = set()
        backtracking([],visited)
        return res


    def permuteUnique_check(self, nums):        
        
        def backtracking(array):
            if len(array) == len(nums):
                res.append(array[:])
                return         
            lastNumber = ""
            for i in range(len(nums)):
                if not visited[i]:
                    if nums[i] != lastNumber:
                        lastNumber = nums[i]
                        visited[i] = True
                        backtracking(array + [nums[i]])
                        visited[i] = False

        nums.sort()
        res = []                
        visited = [False] * len(nums)        
        
        backtracking([])
        return res








