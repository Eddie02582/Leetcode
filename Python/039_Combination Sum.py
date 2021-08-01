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
        
    def combinationSum_dp(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import defaultdict
        dp = defaultdict(list)
        dp[0] = [[]]
        for candidate in candidates:
            for n in range(candidate,target + 1):
                for sub in dp[n - candidate]:                    
                    dp[n].append(sub + [candidate])
        
        return dp[target]