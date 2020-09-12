class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        p,q = 0,0
        ans = []
        while p < len(A) and q < len(B):
            s1,e1 = A[p]
            s2,e2 = B[q]
            if s1 <= s2 <= e1:
                ans.append([s2,min(e1,e2)])
            elif s2 <= s1 <= e2:
                ans.append([s1,min(e1,e2)])          
            if e1 > e2:
                q += 1
            elif e1 < e2:
                p += 1
            else:
                p += 1
                q += 1

        return ans