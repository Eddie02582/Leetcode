class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """    
        visited = set(deadends)
        if "0000" in visited:
            return -1            
        queue = ["0000"]       
        ans = 0
        while queue:
            n = len(queue)          
            for i in range(n):
                s = queue.pop(0)              
                if s == target:                                      
                    return ans
                for j in range(4):
                    up = self.plusOne(s,j)
                    down = self.minusOne(s,j)
                    if up not in visited:
                        visited.add(up)
                        queue.append(up) 
                    down = self.minusOne(s,j)
                    if down not in visited:
                        visited.add(down)
                        queue.append(down)  
            ans += 1       
        return -1
    def plusOne(self,s,j):       
        if s[j] == '9':
            s = s[:j] + "0" + s[j + 1:]          
        else:
            s = s[:j] + chr(ord(s[j]) + 1)   + s[j + 1:]           
        return s
 
    def minusOne(self,s,j):
        if s[j] == '0':
            s = s[:j] + "9" + s[j + 1:]          
        else:
            s = s[:j] + chr(ord(s[j]) - 1)   + s[j + 1:]           
        return s
    
sol = Solution()
sol.openLock(["0201","0101","0102","1212","2002"],"0202")
sol.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"],"8888")
