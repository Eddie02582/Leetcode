class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter   
        return "".join( [ key*cnt for key,cnt in sorted(Counter(s).items(),key = lambda item: -item[1])] )
        
