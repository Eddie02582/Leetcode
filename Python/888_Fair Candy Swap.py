class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        delta = (sum(A) - sum(B))//2
        set_B = set(B)
        
        for n in A:
            if n - delta in set_B:
                return [n,n - delta]



sol =  Solution()   
sol.fairCandySwap([1,1],[2,2])

sol.fairCandySwap([1,2],[2,3])
sol.fairCandySwap([2],[1,3])
sol.fairCandySwap([1,2,5],[2,4])

sol.fairCandySwap([35,17,4,24,10],[63,21])

'''
Output: [1,2]
Output: [1,2]
Output: [2,3]
Output: [1,2]
'''
