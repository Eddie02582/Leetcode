class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        queue = [0]
        
        while queue:
            key = queue.pop(0) 
            visited[key] = True
            for _key in rooms[key]:
                if not visited[_key]:
                    queue.append(_key)              
        
       
        return all(visited)