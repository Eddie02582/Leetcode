class Solution(object):
    def uniqueOccurrences(self, arr):
        count = {}
        for n in arr:
            count[n] =  count.setdefault(n,0) + 1
        return len(set(count.values())) == len(count.values())
        

    def uniqueOccurrences__counter(self, arr):
        from collections import Counter  
        count = Counter(arr).values()        
        return len(set(count)) == len(count)        




sol = Solution()

assert sol.uniqueOccurrences__counter([1,2]) == False

assert sol.uniqueOccurrences__counter([1,2,2,1,1,3]) == True