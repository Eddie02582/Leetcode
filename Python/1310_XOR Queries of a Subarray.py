class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        table = [0] * n        
        temp = 0
        for i in range(n):
            temp = temp ^arr[i]
            table[i] = temp   
       
        ans = []
        for query in queries:
            l,r = query
            if l == 0:
                sol= table[r]
            else:
                sol = table[l -1] ^ table[r]       
            
            ans.append(sol)
        return ans