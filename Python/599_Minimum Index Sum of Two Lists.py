class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indices = {r: i for i, r in enumerate(list1)}
        best, ans = float('inf'), []
        for i, r in enumerate(list2):
            if r not in indices: 
                continue
            if i + indices[r] < best:
                best = i + indices[r]
                ans = [r]
            elif i + indices[r] == best:
                ans.append(r)
        return ans

    def findRestaurant_simply(self, list1: List[str], list2: List[str]) -> List[str]:
        indices = {r: i for i, r in enumerate(list1)}
        best, ans = float('inf'), []
        for i, r in enumerate(list2):
            if r not in indices: 
                continue
            if i + indices[r] < best:
                best = i + indices[r]
                ans = [r]
            elif i + indices[r] == best:
                ans.append(r)
        return ans