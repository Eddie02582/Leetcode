class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x[0])
        n = len(intervals)    
        ans = 0      
        prev = intervals[0]
        for i in range(1,n):
            if prev[1] >intervals[i][0]:
                ans += 1
            else:
                prev = intervals[i]        
        return ans
        

sol = Solution()
sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])