class Solution(object):
    def insert__(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        elif not newInterval:
            return intervals
        
        if newInterval[0] <= intervals[0][0]:
            intervals.insert(0,newInterval)
        elif newInterval[0] >= intervals[-1][0]:
            intervals.append(newInterval)
        
        ans = []
        for interval in intervals:
            if newInterval[0] < interval[0]:
                if not ans or ans[-1][1] < newInterval[0]:
                    ans.append(newInterval)
                else:                
                    ans[-1][1] = max(newInterval[1],ans[-1][1])                  
        
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:                
                ans[-1][1] = max(interval[1],ans[-1][1])          
        
        return ans
            

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        elif not newInterval:
            return intervals
        
        ans  = []
        i,isAppend = 0,False
        while i < len(intervals):
            if not isAppend:
                if newInterval[0] <= intervals[i][0]:
                    intervals.insert(i,newInterval) 
                    isAppend = True
                if i == len(intervals) - 1:
                    intervals.append(newInterval)
                    isAppend = True
            if not ans or ans[-1][1] < intervals[i][0]:
                    ans.append(intervals[i])
            else:                
                ans[-1][1] = max(intervals[i][1],ans[-1][1])                
        
            i += 1

        return ans
            

            
sol = Solution()
sol.insert([[1,5]],[2,7])
sol.insert([[1,3],[6,9]],[2,5])
sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])