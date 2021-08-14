class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import Counter       
        arr.sort(key = lambda x:abs(x))
        counts = Counter(arr)        
        
        for n in arr:
            if counts[n] > 0:
                if counts[2 * n] <= 0:
                    return False           
                counts[n] -= 1
                counts[2 * n] -= 1            
                
        return True