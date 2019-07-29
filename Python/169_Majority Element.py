'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ? n/2 ? times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution(object): 
    def majorityElement_set(self, nums):    
        hash_set =set(nums)  
        
        for n in hash_set:
            if nums.count(n) > len(nums)//2:               
                return n 
                
    def majorityElement_counter(self, nums): 
        from collections import Counter
        counts = Counter(nums)
        return max(counts.keys(),key=counts.get)
                
    def majorityElement__dict(self, nums):
        dic = {}
        for n in nums:
            dic[n] = dic.get(n,0) +1   
            
        for key,value in dic.items():
            if value > len(nums)//2:
                return key         
        #return max(dic.keys(),key=dic.get)
      

    def majorityElement_sort(self, nums):
        nums.sort()
        count  = 0
        pre_n = nums[0]
        
        for n in nums[:]:
            if pre_n == n:
                count += 1
            else:
                count = 1
            if count >= len(nums)/2:
                return n
            pre_n = n   

    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
        
    def majorityElement_Boyer_Moore(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            #count += (1 if num == candidate else -1)
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate        
        
        
    
sol= Solution()

assert sol.majorityElement_Boyer_Moore([3,2,3]) == 3

assert sol.majorityElement_Boyer_Moore([2,2,1,1,1,2,2]) == 2



