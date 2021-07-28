class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:        
        from collections import deque
        lookup = {e.id: e for e in employees}
        queue = deque([lookup[id]])
        total = 0
        while queue:
            e = queue.popleft()
            total += e.importance
            queue += map(lookup.get, e.subordinates)
        return total 
        
        
        
        
