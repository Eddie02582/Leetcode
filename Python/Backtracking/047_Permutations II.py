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











