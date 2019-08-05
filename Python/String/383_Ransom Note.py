class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for s in magazine:
            count[s] = count.setdefault(s,0) + 1
        
        for s in ransomNote:
            if count.setdefault(s,0) <= 0:
                return False
            count[s] -=1
        
        return True   
    
    
    def canConstruct_set(self, ransomNote, magazine):
        for s in set(ransomNote):
            if ransomNote.count(s) > magazine.count(s):
                return False
        return True  
        

sol = Solution()

assert sol.canConstruct_set("a",'b') == False

assert sol.canConstruct_set("aa",'ab') == False

assert sol.canConstruct_set("aa",'aab') == False