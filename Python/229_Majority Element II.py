'''
Given an integer array of size n, find all elements that appear more than ? n/3 ? times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

class Solution(object):
    def majorityElement(self, nums):  
        hash_set =set(nums)                  
        return [ n for n in hash_set if nums.count(n) > len(nums)//3] 
                
    def majorityElement__dict(self, nums):
        dic = {}
        for n in nums:
            dic[n] = dic.get(n,0) +1 
            
        return [key  for key,value in dic.items() if value > len(nums)//3]    
        
    def majorityElement_counter(self, nums):
        from collections import Counter
        return [key  for key,value in Counter(nums).items() if value > len(nums)//3]    
        
    def majorityElement_counter__moore(self, nums):
        N = len(nums)
        m = n = cm = cn = 0
        for num in nums:
            if num == m:
                cm += 1
            elif num == n:
                cn += 1
            elif cm == 0:
                m = num
                cm = 1
            elif cn == 0:
                n = num
                cn = 1
            else:
                cm -= 1
                cn -= 1
        cm = cn = 0
        for num in nums:
            if num == m:
                cm += 1
            elif num == n:
                cn += 1
        res = []
        if cm > N / 3:
            res.append(m)
        if cn > N / 3:
            res.append(n)
        return res

        
  
        
        
    
sol= Solution()

assert sol.majorityElement_Boyer_Moore([3,2,3]) == 3

assert sol.majorityElement_Boyer_Moore([2,2,1,1,1,2,2]) == 2



