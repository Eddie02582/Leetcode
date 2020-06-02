# Merge Intervals

## 原題目:
```
Given a collection of intervals, merge all overlapping intervals.

Example 1:

    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

## 思路1
先排序,排序完只剩2種情況interval起始値在不在前一個區間<br> 
1.當res = [] 或是當interval起始値不在res[-1]的區間,這種時候直接添加<br>
2.當interval起始為置在res[-1]區間時,需要取得最大的結束位置

#### Python

``` python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #if is sort 
        if not intervals:
            return []
        intervals.sort()
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1],interval[1])        
        return res 
``` 



