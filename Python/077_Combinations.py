class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if  n <= 0 or n < k:
            return []

        def dfs(curr,level):
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(level,n + 1):
                curr.append(i)
                dfs(curr,i + 1)
                curr.pop()

        curr = []
        dfs(curr,1)

        return res

    def combine(self, n, k):
        def backtrack(path, start):
            if len(path) == k:
                res.append(path)
            for i in range(start, n+1):
                backtrack(path + [i], i + 1)
        
        res = []
        backtrack([], 1)
        return res        
