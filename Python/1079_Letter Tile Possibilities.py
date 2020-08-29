class Solution(object):        
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        from collections import Counter
        
        count = Counter(tiles)
        self.ans = 0
        
        def backtracking(s):          
            for key in count.keys():
                if count[key] >0:
                    count[key] -= 1
                    self.ans += 1
                    backtracking(s + key)                
                    count[key] += 1
        backtracking()
        return self.ans
        
sol = Solution()
sol.numTilePossibilities("AAABBC")