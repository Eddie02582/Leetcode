class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtracking(array,start):
            if sum(array) == target:
                res.append(array[:])
                return
            elif sum(array) > target:
                return
            for i in range (start,len(candidates)): 
                n = candidates[i]              
                backtracking(array + [n],i)

        res = []    
        backtracking([],0)    
        return res