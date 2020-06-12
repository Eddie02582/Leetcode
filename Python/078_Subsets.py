class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = [[]]
        
        for num in nums:
            temp = []
            for curr in output:
                temp.append(curr + [num])  
            output += temp
        return output
            

    def subsets_backtrack(self, nums):
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()  
        return output
        

    def subsets_bitmask(self, nums):
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output          

    def subsets_itertools(self, nums: List[int]) -> List[List[int]]:
        import itertools
        res = []
        for i in range(0,len(nums) + 1):
            res += list(itertools.combinations(nums, i))
        return res   

    def subsets_mask(self, nums):        
        def backtrack(count = 0,curr =[]):            
            if len(nums) == count:                 
                res.append(curr[:])
                return  
            backtrack(count + 1,curr)           
            backtrack(count + 1,curr + [nums[count]]) 

        res = [] 
        n = len(nums)
        backtrack(0,[])  
        return res        
        
        
        