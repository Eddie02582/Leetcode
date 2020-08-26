'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

    Input: [2,2,3,2]
    Output: 3
    
Example 2:

    Input: [0,1,0,1,0,1,99]
    Output: 99

'''

class Solution(object):
    def singleNumber_counter(self, nums):
        from collections import Counter
        counter = Counter(nums)
        return [ key for key in counter.keys() if counter[key]==3][-1]
        
        
    def singleNumber_sum(self, nums):        
        return (3*sum(set(nums))-sum(nums))/2

    '''
         I think this is generalize verson of #135. Where use xor bit operater.
        Since each bit only contains 2 state, for 3 state, you need two bits m1, m2.
        Then for each bit, you just need to build bit operators which does,
        When input is 1, change in these order
        m1 0 -> 0 -> 1 -> 0
        m2 0 -> 1 -> 0 -> 0
        and, when input bit is 0, don't change the state.
        (you don't need to consider m1,m2 = 1,1)     
    
    '''



    def singleNumber(self, nums) :
        # Use two bit operater
        m1, m2 = 0, 0
        # n = 1
        # m1 0 0 1 0
        # m2 0 1 0 0
        # n = 0, remain it same
        for n in nums:
            tmp = m1
            m1 = m1 ^ n&(m1 ^ m2)
            m2 = m2 ^ n&(~tmp)
            #print(n, m1, m2)
        return m2
        
        
    def singleNumber_compare(self, nums):        
        nums.sort()
        for i in range(0,len(nums),3):
            if len(nums) <= i+1:
                return nums[i] 
            elif nums[i] != nums[i+1] or nums[i] != nums[i+2]:
                return nums[i] 
            
        
        
        
        
        
        
sol =  Solution()
assert sol.singleNumber_compare([2,2,3,2])==3      
assert sol.singleNumber_compare([0,1,0,1,0,1,99])==99       

assert sol.singleNumber_compare([1,2,5,2,5,5,2])==1        
   