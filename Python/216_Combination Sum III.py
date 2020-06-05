class Solution:
    def combinationSum3(self, k,n):     
        
        def backtracking(array,start,target):
            if target == 0 and len(array) == k:
                res.append(array[:])
                return        
            elif target < 0  or len(array) > k:
                return   
            for i in range(start,end):  
                backtracking(array + [i], i + 1 ,target - i)
                   

        res = []
        end = 10
        if n < end:
            end = n + 1

        backtracking([],1,n)
        return res